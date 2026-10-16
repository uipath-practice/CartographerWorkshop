"""Resolve lesson context for each image."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Optional

import numpy as np

from .config import DOCS_ROOT, VECTOR_STORE_PATH
from .image_scanner import ImageTask


@lru_cache(maxsize=64)
def _read_file(path: Path) -> str:
    """Read and cache a text file."""
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""


def _extract_title(markdown: str) -> str:
    """Extract the H1 title from markdown content."""
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip()
    return ""


def _find_image_context(markdown: str, image_name: str, window: int = 10) -> str:
    """Find the markdown lines surrounding an image reference.

    Returns the lines within `window` lines before and after the image reference.
    """
    lines = markdown.splitlines()
    # Find lines referencing this image (by filename)
    indices = [
        i for i, line in enumerate(lines) if image_name in line
    ]

    if not indices:
        return ""

    # Take the first reference
    idx = indices[0]
    start = max(0, idx - window)
    end = min(len(lines), idx + window + 1)
    return "\n".join(lines[start:end])


def _extract_alt_text(markdown: str, image_name: str) -> str:
    """Extract the alt text for an image from markdown."""
    pattern = rf"!\[([^\]]*)\]\([^)]*{re.escape(image_name)}[^)]*\)"
    match = re.search(pattern, markdown)
    return match.group(1) if match else ""


def _extract_section_heading(markdown: str, image_name: str) -> str:
    """Find the heading under which an image appears."""
    lines = markdown.splitlines()
    last_heading = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            last_heading = stripped.lstrip("#").strip()
        if image_name in stripped:
            return last_heading
    return last_heading


class VectorStore:
    """Simple vector store for context retrieval."""

    def __init__(self):
        self.chunks: list[dict] = []
        self.embeddings: Optional[np.ndarray] = None
        self._loaded = False

    def load(self) -> bool:
        """Load the vector store from disk. Returns True if loaded."""
        if self._loaded:
            return self.embeddings is not None

        self._loaded = True
        if not VECTOR_STORE_PATH.exists():
            return False

        data = json.loads(VECTOR_STORE_PATH.read_text(encoding="utf-8"))
        self.chunks = data.get("chunks", [])
        embeddings_list = [c["embedding"] for c in self.chunks if "embedding" in c]
        if embeddings_list:
            self.embeddings = np.array(embeddings_list, dtype=np.float32)
            return True
        return False

    def query(self, query_embedding: list[float], top_k: int = 2) -> list[dict]:
        """Find the top-K most similar chunks by cosine similarity."""
        if self.embeddings is None or len(self.chunks) == 0:
            return []

        query_vec = np.array(query_embedding, dtype=np.float32)
        # Cosine similarity
        norms = np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vec)
        norms = np.maximum(norms, 1e-10)
        similarities = self.embeddings @ query_vec / norms
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [
            {"text": self.chunks[i]["text"], "source": self.chunks[i].get("source", ""), "score": float(similarities[i])}
            for i in top_indices
        ]


# Module-level vector store instance
_vector_store = VectorStore()


def resolve_context(
    task: ImageTask,
    embedding_client=None,
    doc_chunks: Optional[list] = None,
) -> dict:
    """Resolve full context for an image task.

    Args:
        task: The ImageTask to resolve context for.
        embedding_client: Optional Azure OpenAI client for vector store queries.
        doc_chunks: Optional list of pre-embedded documentation chunks from
            the exercise's documentation.md. Provided by doc_context.update_doc_context().

    Returns:
        Dict with keys: lesson_title, exercise_name, lesson_context, alt_text,
        section_heading, rag_context.
    """
    from .doc_context import query_doc_chunks

    # Find the lesson markdown file
    lesson_md_path = task.image_path.parent.parent / f"{task.lesson_slug}.md"
    lesson_content = _read_file(lesson_md_path)

    # Find the exercise overview
    exercise_index_path = DOCS_ROOT / task.exercise_slug / "index.md"
    exercise_content = _read_file(exercise_index_path)

    # Extract structured context
    lesson_title = _extract_title(lesson_content) or task.lesson_slug
    exercise_name = _extract_title(exercise_content) or task.exercise_slug
    alt_text = _extract_alt_text(lesson_content, task.image_name)
    section_heading = _extract_section_heading(lesson_content, task.image_name)
    surrounding_context = _find_image_context(lesson_content, task.image_name, window=10)

    # Build the context string
    context_parts = []
    if exercise_name:
        context_parts.append(f"Exercise: {exercise_name}")
    if section_heading:
        context_parts.append(f"Section: {section_heading}")
    if alt_text:
        context_parts.append(f"Image alt text: {alt_text}")
    if surrounding_context:
        context_parts.append(f"Surrounding lesson content:\n{surrounding_context}")

    # Compute query embedding once, used for both vector store and doc chunks
    query_embedding = None
    rag_context = ""
    if embedding_client:
        query_text = f"{lesson_title} {section_heading} {alt_text}"
        try:
            from .config import AZURE_EMBEDDING_DEPLOYMENT

            resp = embedding_client.embeddings.create(
                model=AZURE_EMBEDDING_DEPLOYMENT,
                input=query_text,
            )
            query_embedding = resp.data[0].embedding
        except Exception as e:
            print(f"  Warning: Embedding query failed: {e}")

    # Vector store RAG
    if query_embedding:
        _vector_store.load()
        if _vector_store.embeddings is not None:
            try:
                results = _vector_store.query(query_embedding, top_k=2)
                if results:
                    rag_parts = [
                        f"[From: {r['source']}]\n{r['text']}"
                        for r in results
                        if r["score"] > 0.3
                    ]
                    if rag_parts:
                        rag_context = "\n---\n".join(rag_parts)
                        context_parts.append(
                            f"Additional reference context:\n{rag_context}"
                        )
            except Exception as e:
                print(f"  Warning: RAG query failed: {e}")

    # Documentation context (exercise-specific doc pages)
    if doc_chunks and query_embedding:
        try:
            doc_results = query_doc_chunks(doc_chunks, query_embedding, top_k=3)
            if doc_results:
                doc_parts = [
                    f"[Official docs: {r['source']}]\n{r['text']}"
                    for r in doc_results
                ]
                context_parts.append(
                    f"Official UiPath documentation context:\n" + "\n---\n".join(doc_parts)
                )
        except Exception as e:
            print(f"  Warning: Doc context query failed: {e}")

    lesson_context = "\n\n".join(context_parts)

    return {
        "lesson_title": lesson_title,
        "exercise_name": exercise_name,
        "lesson_context": lesson_context,
        "alt_text": alt_text,
        "section_heading": section_heading,
        "rag_context": rag_context,
    }
