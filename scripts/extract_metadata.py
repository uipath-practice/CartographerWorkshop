"""Main CLI entry point for screenshot metadata extraction."""

from __future__ import annotations

import argparse
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

from .config import DOCS_ROOT, get_openai_client
from .context_resolver import resolve_context
from .doc_context import update_doc_context
from .image_scanner import ImageTask, scan_images
from .llm_client import build_prompt, extract_from_image
from .metadata_writer import build_metadata, write_metadata


def process_image(
    client,
    task: ImageTask,
    embedding_client=None,
    doc_chunks: Optional[list] = None,
    verbose: bool = False,
) -> dict:
    """Process a single image: resolve context, call LLM, write metadata.

    Returns a result dict with status and token usage.
    """
    try:
        # Resolve context
        context = resolve_context(
            task,
            embedding_client=embedding_client,
            doc_chunks=doc_chunks,
        )

        # Build prompt
        system_prompt = build_prompt(
            lesson_title=context["lesson_title"],
            exercise_name=context["exercise_name"],
            lesson_context=context["lesson_context"],
        )

        if verbose:
            print(f"  Context: {context['lesson_title']} / {context['section_heading']}")

        # Call LLM
        extraction, usage = extract_from_image(client, task.image_path, system_prompt)

        # Build and write metadata
        metadata = build_metadata(task, extraction, usage)
        write_metadata(task.metadata_path, metadata)

        return {
            "status": "success",
            "image": task.image_name,
            "tokens": usage["total_tokens"],
        }

    except Exception as e:
        return {
            "status": "error",
            "image": task.image_name,
            "error": str(e),
            "tokens": 0,
        }


def main():
    parser = argparse.ArgumentParser(
        description="Extract metadata from course screenshots using Azure OpenAI GPT-5.4.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python -m scripts.extract_metadata --dry-run
  python -m scripts.extract_metadata --image docs/warranty-resolution/index.images/new-project-dialog-W.png
  python -m scripts.extract_metadata --folder docs/warranty-resolution/
  python -m scripts.extract_metadata --force --verbose
""",
    )
    parser.add_argument(
        "--folder",
        type=Path,
        default=None,
        help=f"Folder to scan for images (default: {DOCS_ROOT})",
    )
    parser.add_argument(
        "--image",
        type=Path,
        default=None,
        help="Process a single image file.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate metadata even if it already exists.",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=3,
        help="Maximum concurrent API calls (default: 3).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List images that would be processed without calling the API.",
    )
    parser.add_argument(
        "--skip-assets",
        action="store_true",
        default=True,
        help="Skip docs/assets/images/ (default: True).",
    )
    parser.add_argument(
        "--no-skip-assets",
        action="store_false",
        dest="skip_assets",
        help="Include docs/assets/images/ in processing.",
    )
    parser.add_argument(
        "--no-rag",
        action="store_true",
        help="Disable RAG context (skip vector store queries).",
    )
    parser.add_argument(
        "--no-doc-context",
        action="store_true",
        help="Skip loading documentation context from documentation.txt.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed progress.",
    )
    args = parser.parse_args()

    # Scan for images
    tasks = scan_images(
        folder=args.folder,
        force=args.force,
        skip_assets=args.skip_assets,
        single_image=args.image,
    )

    if not tasks:
        print("No images to process.")
        return

    # Dry run mode
    if args.dry_run:
        print(f"Found {len(tasks)} images to process:\n")
        for t in tasks:
            print(f"  {t.relative_image_path}")
            print(f"    -> {t.metadata_path.name}")
            print(f"    Lesson: {t.lesson_slug}, Exercise: {t.exercise_slug}")
            print()
        return

    # Initialize clients
    client = get_openai_client()
    embedding_client = None if args.no_rag else client

    # Load documentation context per exercise (before processing images)
    doc_chunks_by_exercise: dict = {}
    if not args.no_doc_context:
        exercise_slugs = {task.exercise_slug for task in tasks if task.exercise_slug}
        for slug in sorted(exercise_slugs):
            exercise_folder = DOCS_ROOT / slug
            doc_md = exercise_folder / "documentation.txt"
            if doc_md.exists():
                print(f"Updating documentation context for: {slug}")
                chunks = update_doc_context(exercise_folder)
                doc_chunks_by_exercise[slug] = chunks
                if chunks:
                    print(f"  {len(chunks)} doc context chunks ready")
                print()

    # Process images
    total = len(tasks)
    print(f"Processing {total} images with concurrency={args.concurrency}...\n")

    results = []
    start_time = time.time()

    if args.concurrency == 1 or total == 1:
        # Sequential processing
        for i, task in enumerate(tasks, 1):
            print(f"[{i}/{total}] {task.image_name}")
            doc_chunks = doc_chunks_by_exercise.get(task.exercise_slug, [])
            result = process_image(
                client,
                task,
                embedding_client=embedding_client,
                doc_chunks=doc_chunks,
                verbose=args.verbose,
            )
            results.append(result)
            if result["status"] == "success":
                print(f"  Done ({result['tokens']} tokens)")
            else:
                print(f"  ERROR: {result['error']}")
    else:
        # Concurrent processing
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            future_to_task = {
                executor.submit(
                    process_image,
                    client,
                    task,
                    embedding_client=embedding_client,
                    doc_chunks=doc_chunks_by_exercise.get(task.exercise_slug, []),
                    verbose=args.verbose,
                ): task
                for task in tasks
            }

            completed = 0
            for future in as_completed(future_to_task):
                completed += 1
                task = future_to_task[future]
                result = future.result()
                results.append(result)

                if result["status"] == "success":
                    print(f"[{completed}/{total}] {task.image_name} - Done ({result['tokens']} tokens)")
                else:
                    print(f"[{completed}/{total}] {task.image_name} - ERROR: {result['error']}")

    # Summary
    elapsed = time.time() - start_time
    success = sum(1 for r in results if r["status"] == "success")
    errors = sum(1 for r in results if r["status"] == "error")
    total_tokens = sum(r["tokens"] for r in results)

    print(f"\n{'='*50}")
    print(f"Completed in {elapsed:.1f}s")
    print(f"  Processed: {success}")
    print(f"  Errors:    {errors}")
    print(f"  Tokens:    {total_tokens:,}")

    if errors:
        print(f"\nFailed images:")
        for r in results:
            if r["status"] == "error":
                print(f"  {r['image']}: {r['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
