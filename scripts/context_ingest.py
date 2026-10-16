"""Context ingestion pipeline — process documents and build vector store."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import requests
from bs4 import BeautifulSoup

from .config import (
    AZURE_EMBEDDING_DEPLOYMENT,
    CONTEXT_DIR,
    DOCS_ROOT,
    VECTOR_STORE_PATH,
    get_openai_client,
)

# Chunking parameters
CHUNK_SIZE = 500  # approximate tokens (using ~4 chars per token heuristic)
CHUNK_OVERLAP = 50
CHARS_PER_TOKEN = 4


def _chunk_text(text: str, source: str) -> list[dict]:
    """Split text into overlapping chunks.

    Uses a simple character-based approach with ~4 chars per token heuristic.
    """
    chunk_chars = CHUNK_SIZE * CHARS_PER_TOKEN
    overlap_chars = CHUNK_OVERLAP * CHARS_PER_TOKEN
    chunks = []

    # Split by paragraphs first for cleaner breaks
    paragraphs = text.split("\n\n")
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 > chunk_chars and current:
            chunks.append({"text": current.strip(), "source": source})
            # Keep overlap from end of current chunk
            current = current[-overlap_chars:] + "\n\n" + para
        else:
            current = current + "\n\n" + para if current else para

    if current.strip():
        chunks.append({"text": current.strip(), "source": source})

    return chunks


def _extract_pdf_text(pdf_path: Path) -> str:
    """Extract text from a PDF file."""
    try:
        import pdfplumber

        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n\n".join(text_parts)
    except ImportError:
        print(f"  Warning: pdfplumber not installed, skipping {pdf_path.name}")
        return ""
    except Exception as e:
        print(f"  Error processing PDF {pdf_path.name}: {e}")
        return ""


def _fetch_url_content(url: str) -> str:
    """Fetch a web page and extract its main text content."""
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove script and style elements
        for tag in soup(["script", "style", "nav", "header", "footer"]):
            tag.decompose()

        # Try to find main content area
        main = soup.find("main") or soup.find("article") or soup.find("body")
        if main:
            return main.get_text(separator="\n", strip=True)
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        print(f"  Error fetching URL {url}: {e}")
        return ""


def _collect_documents() -> list[dict]:
    """Collect all documents to ingest.

    Returns list of dicts with keys: text, source.
    """
    documents = []

    # 1. Ingest lesson markdown files from docs/
    for md_path in sorted(DOCS_ROOT.rglob("*.md")):
        # Skip files in site/ output
        try:
            md_path.relative_to(DOCS_ROOT.parent / "site")
            continue
        except ValueError:
            pass

        text = md_path.read_text(encoding="utf-8")
        if text.strip():
            relative = str(md_path.relative_to(DOCS_ROOT))
            documents.append({"text": text, "source": f"docs/{relative}"})

    # 2. Ingest external context documents
    if CONTEXT_DIR.exists():
        for file_path in sorted(CONTEXT_DIR.iterdir()):
            if file_path.name in ("README.md", "vector_store.json"):
                continue

            if file_path.suffix == ".pdf":
                text = _extract_pdf_text(file_path)
                if text:
                    documents.append({"text": text, "source": file_path.name})

            elif file_path.suffix in (".txt", ".md"):
                text = file_path.read_text(encoding="utf-8")
                if text.strip():
                    documents.append({"text": text, "source": file_path.name})

            elif file_path.suffix == ".url":
                url = file_path.read_text(encoding="utf-8").strip()
                if url:
                    print(f"  Fetching {url}...")
                    text = _fetch_url_content(url)
                    if text:
                        documents.append({"text": text, "source": url})

    return documents


def _embed_chunks(chunks: list[dict]) -> list[dict]:
    """Add embeddings to each chunk using Azure OpenAI."""
    if not chunks:
        return chunks

    client = get_openai_client()
    batch_size = 16
    total = len(chunks)

    for i in range(0, total, batch_size):
        batch = chunks[i : i + batch_size]
        texts = [c["text"] for c in batch]

        print(f"  Embedding chunks {i + 1}-{min(i + batch_size, total)} of {total}...")

        response = client.embeddings.create(
            model=AZURE_EMBEDDING_DEPLOYMENT,
            input=texts,
        )

        for j, item in enumerate(response.data):
            chunks[i + j]["embedding"] = item.embedding

    return chunks


def build_vector_store(rebuild: bool = False) -> None:
    """Build the vector store from all context documents.

    Args:
        rebuild: If True, rebuild even if vector_store.json exists.
    """
    if VECTOR_STORE_PATH.exists() and not rebuild:
        print(f"Vector store already exists at {VECTOR_STORE_PATH}")
        print("Use --rebuild to regenerate.")
        return

    print("Collecting documents...")
    documents = _collect_documents()
    print(f"  Found {len(documents)} documents")

    if not documents:
        print("No documents to process.")
        return

    print("Chunking documents...")
    all_chunks = []
    for doc in documents:
        chunks = _chunk_text(doc["text"], doc["source"])
        all_chunks.extend(chunks)
    print(f"  Created {len(all_chunks)} chunks")

    print("Generating embeddings...")
    all_chunks = _embed_chunks(all_chunks)

    # Save vector store
    CONTEXT_DIR.mkdir(parents=True, exist_ok=True)
    store_data = {"chunks": all_chunks}
    VECTOR_STORE_PATH.write_text(
        json.dumps(store_data, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Vector store saved to {VECTOR_STORE_PATH} ({len(all_chunks)} chunks)")


def main():
    parser = argparse.ArgumentParser(
        description="Ingest context documents and build the vector store."
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Rebuild the vector store even if it already exists.",
    )
    parser.add_argument(
        "--context-dir",
        type=Path,
        default=None,
        help="Override the context directory path.",
    )
    args = parser.parse_args()

    if args.context_dir:
        import scripts.config as cfg

        cfg.CONTEXT_DIR = args.context_dir

    build_vector_store(rebuild=args.rebuild)


if __name__ == "__main__":
    main()
