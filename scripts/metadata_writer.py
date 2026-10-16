"""Write metadata JSON files atomically."""

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

from .config import AZURE_API_VERSION, AZURE_DEPLOYMENT, METADATA_SUFFIX


def classify_layout_mode(image_path: Path, ocr_text: str) -> dict:
    """Classify image layout mode based on OCR text volume and aspect ratio.

    Analyzes the image to determine optimal display:
    - "full_width": Full-screen UI with detailed layout (use width="900")
    - "split_50": Medium density, balanced split (use |50|)
    - "split_30": Compact UI, narrow panel (use |30|)

    Returns:
        Dict with keys: mode, ocr_length, aspect_ratio, rationale.
    """
    try:
        # Get image dimensions
        img = Image.open(image_path)
        width, height = img.size
        aspect_ratio = width / height if height > 0 else 1.0

        # Analyze OCR text
        ocr_length = len(ocr_text.strip())

        # Classification logic
        # Full-screen UIs: either high text + wide aspect, or very high text volume
        if (ocr_length > 600 and aspect_ratio > 1.4) or ocr_length > 1200:
            mode = "full_width"
            rationale = f"High density ({ocr_length} chars) + wide ({aspect_ratio:.2f}) or very high text"
        # Medium density: substantial text content
        elif ocr_length > 300:
            mode = "split_50"
            rationale = f"Medium text density ({ocr_length} chars)"
        # Compact: little text or tall/narrow aspect
        else:
            mode = "split_30"
            rationale = f"Low text density ({ocr_length} chars) or narrow layout"

        return {
            "mode": mode,
            "ocr_length": ocr_length,
            "aspect_ratio": round(aspect_ratio, 2),
            "image_size": f"{width}x{height}",
            "rationale": rationale,
        }

    except Exception as e:
        # Fallback to split_30 if image can't be analyzed
        return {
            "mode": "split_30",
            "ocr_length": len(ocr_text.strip()) if ocr_text else 0,
            "aspect_ratio": None,
            "image_size": None,
            "rationale": f"Error analyzing image: {str(e)}",
        }


def build_metadata(
    image_task,
    extraction: dict,
    usage: dict,
) -> dict:
    """Build the full metadata dictionary.

    Args:
        image_task: The ImageTask being processed.
        extraction: Dict with keys: ocr_text, description, step_instructions.
        usage: Dict with keys: prompt_tokens, completion_tokens, total_tokens.

    Returns:
        Complete metadata dictionary ready to write.
    """
    # Classify layout mode based on image and OCR
    ocr_text = extraction.get("ocr_text", "")
    layout_info = classify_layout_mode(image_task.image_path, ocr_text)

    return {
        "version": "1.0",
        "image_file": image_task.image_name,
        "image_path": image_task.relative_image_path,
        "lesson": image_task.lesson_slug,
        "exercise": image_task.exercise_slug,
        "extraction": {
            "ocr_text": ocr_text,
            "description": extraction.get("description", ""),
            "step_instructions": extraction.get("step_instructions", ""),
        },
        "layout": layout_info,
        "model": {
            "name": "gpt-5.4",
            "deployment": AZURE_DEPLOYMENT,
            "api_version": AZURE_API_VERSION,
        },
        "usage": {
            "prompt_tokens": usage.get("prompt_tokens", 0),
            "completion_tokens": usage.get("completion_tokens", 0),
            "total_tokens": usage.get("total_tokens", 0),
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def write_metadata(metadata_path: Path, metadata: dict) -> None:
    """Write metadata to a JSON file atomically.

    Writes to a temporary file first, then renames to avoid partial writes.
    """
    content = json.dumps(metadata, indent=2, ensure_ascii=False) + "\n"

    # Write to temp file in the same directory, then rename
    fd, tmp_path = tempfile.mkstemp(
        dir=metadata_path.parent,
        suffix=".tmp",
        prefix=metadata_path.stem,
    )
    try:
        with open(fd, "w", encoding="utf-8") as f:
            f.write(content)
        Path(tmp_path).replace(metadata_path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise
