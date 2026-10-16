"""Per-exercise documentation context: fetch, embed, and cache URL content.

Reads documentation.txt from an exercise folder, fetches text from each URL,
embeds the content using Azure OpenAI text-embedding-3-small, and caches
results in documentation.cache.json. Only new URLs (not yet cached) are
fetched and embedded on subsequent runs.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import requests
from bs4 import BeautifulSoup

from .config import AZURE_EMBEDDING_DEPLOYMENT, get_openai_client

DOC_FILENAME = "documentation.txt"
CACHE_FILENAME = "documentation.cache.json"

# Match context_ingest.py chunking parameters
CHUNK_SIZE = 500        # approximate tokens
CHUNK_OVERLAP = 50
CHARS_PER_TOKEN = 4


# ---------------------------------------------------------------------------
# Text extraction
# ---------------------------------------------------------------------------

def _extract_urls(doc_path: Path) -> list[str]:
    """Parse documentation.txt and return all URLs in order, deduplicated."""
    if not doc_path.exists():
        return []
    text = doc_path.read_text(encoding="utf-8")
    seen: set[str] = set()
    urls: list[str] = []
    for match in re.finditer(r"https?://[^\s)\]>\"']+", text):
        url = match.group(0).rstrip(".,;")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def _fetch_url_text(url: str) -> str:
    """Fetch a URL and return clean plain text (no images, no scripts)."""
    try:
        resp = requests.get(
            url,
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer"]):
            tag.decompose()
        main = soup.find("main") or soup.find("article") or soup.find("body")
        if main:
            return main.get_text(separator="\n", strip=True)
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        print(f"  Warning: Could not fetch {url}: {e}")
        return ""


# ---------------------------------------------------------------------------
# Chunking
# ---------------------------------------------------------------------------

def _chunk_text(text: str, source: str) -> list[dict]:
    """Split text into overlapping chunks with paragraph-aware breaks."""
    chunk_chars = CHUNK_SIZE * CHARS_PER_TOKEN
    overlap_chars = CHUNK_OVERLAP * CHARS_PER_TOKEN
    chunks: list[dict] = []
    paragraphs = text.split("\n\n")
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 > chunk_chars and current:
            chunks.append({"text": current.strip(), "source": source})
            current = current[-overlap_chars:] + "\n\n" + para
        else:
            current = current + "\n\n" + para if current else para

    if current.strip():
        chunks.append({"text": current.strip(), "source": source})

    return chunks


# ---------------------------------------------------------------------------
# Embedding
# ---------------------------------------------------------------------------

def _embed_chunks(chunks: list[dict]) -> list[dict]:
    """Add 'embedding' list to each chunk dict in place."""
    if not chunks:
        return chunks

    client = get_openai_client()
    batch_size = 16
    total = len(chunks)

    for i in range(0, total, batch_size):
        batch = chunks[i: i + batch_size]
        texts = [c["text"] for c in batch]
        end = min(i + batch_size, total)
        print(f"    Embedding doc chunks {i + 1}–{end} of {total}...")
        response = client.embeddings.create(
            model=AZURE_EMBEDDING_DEPLOYMENT,
            input=texts,
        )
        for j, item in enumerate(response.data):
            chunks[i + j]["embedding"] = item.embedding

    return chunks


# ---------------------------------------------------------------------------
# Cache I/O
# ---------------------------------------------------------------------------

def _load_cache(cache_path: Path) -> dict:
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {"embedded_urls": {}}


def _save_cache(cache_path: Path, cache: dict) -> None:
    cache_path.write_text(
        json.dumps(cache, ensure_ascii=False),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def update_doc_context(exercise_folder: Path) -> list[dict]:
    """Update the documentation cache and return all embedded chunks.

    Reads documentation.txt from the exercise folder. For each URL not already
    in the cache, fetches text content, chunks it, embeds it, and saves to
    documentation.cache.json. Returns all embedded chunks (cached + new) for
    use as RAG context during image extraction.

    Args:
        exercise_folder: Path to the exercise folder
                         (e.g. docs/warranty-resolution/).

    Returns:
        List of chunk dicts with keys: text, source, embedding.
        Empty list if documentation.txt is missing or has no URLs.
    """
    doc_path = exercise_folder / DOC_FILENAME
    cache_path = exercise_folder / CACHE_FILENAME

    urls = _extract_urls(doc_path)
    if not urls:
        return []

    cache = _load_cache(cache_path)
    all_chunks: list[dict] = []
    new_count = 0

    for url in urls:
        if url in cache["embedded_urls"]:
            # Already cached — collect without re-fetching
            all_chunks.extend(cache["embedded_urls"][url]["chunks"])
            continue

        # New URL: fetch → chunk → embed → cache
        print(f"  Fetching: {url}")
        text = _fetch_url_text(url)
        if not text:
            print(f"  Skipping (empty response): {url}")
            continue

        chunks = _chunk_text(text, url)
        chunks = _embed_chunks(chunks)

        if chunks:
            cache["embedded_urls"][url] = {
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "chunks": chunks,
            }
            all_chunks.extend(chunks)
            new_count += 1

    if new_count:
        _save_cache(cache_path, cache)
        print(f"  Cached {new_count} new URL(s) → {cache_path.name}")

    return all_chunks


def query_doc_chunks(
    doc_chunks: list[dict],
    query_embedding: list[float],
    top_k: int = 3,
    min_score: float = 0.3,
) -> list[dict]:
    """Return the top-k most relevant doc chunks by cosine similarity.

    Args:
        doc_chunks: List of chunk dicts with 'embedding', 'text', 'source'.
        query_embedding: Query vector.
        top_k: Maximum number of results to return.
        min_score: Minimum cosine similarity threshold.

    Returns:
        List of dicts with keys: text, source, score.
    """
    valid = [c for c in doc_chunks if "embedding" in c]
    if not valid:
        return []

    embeddings = np.array([c["embedding"] for c in valid], dtype=np.float32)
    query_vec = np.array(query_embedding, dtype=np.float32)

    norms = np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_vec)
    norms = np.maximum(norms, 1e-10)
    similarities = embeddings @ query_vec / norms

    k = min(top_k, len(valid))
    top_indices = np.argsort(similarities)[-k:][::-1]

    return [
        {
            "text": valid[i]["text"],
            "source": valid[i]["source"],
            "score": float(similarities[i]),
        }
        for i in top_indices
        if similarities[i] >= min_score
    ]
