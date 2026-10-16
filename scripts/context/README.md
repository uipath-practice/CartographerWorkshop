# Context Documents

Place external context documents here for the RAG pipeline.

## Supported file types

| Extension | Processing |
|-----------|------------|
| `.pdf`    | Text extracted page-by-page via pdfplumber |
| `.txt`    | Read as plain text |
| `.md`     | Read as plain text (Markdown) |
| `.url`    | Text file containing a single URL — page is fetched and main content extracted |

## Usage

1. Add your context documents to this folder.
2. Run the ingestion pipeline:
   ```bash
   python -m scripts.context_ingest
   ```
3. This builds `vector_store.json` (gitignored) which is used automatically during image extraction.

Lesson markdown files from `docs/` are also ingested automatically.
