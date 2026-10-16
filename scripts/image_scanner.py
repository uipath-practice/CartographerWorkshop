"""Discover images in docs/ and resolve metadata paths."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .config import DOCS_ROOT, METADATA_SUFFIX, SKIP_DIRS, SUPPORTED_EXTENSIONS


@dataclass
class ImageTask:
    """Represents an image to process."""

    image_path: Path
    metadata_path: Path
    lesson_slug: str
    exercise_slug: str
    image_name: str

    @property
    def relative_image_path(self) -> str:
        """Image path relative to project root."""
        return str(self.image_path.relative_to(DOCS_ROOT.parent))


def _resolve_lesson_slug(image_dir: Path) -> str:
    """Map an image directory to its lesson slug.

    Image dirs follow the pattern: <step-slug>.images/
    e.g. configure-agent.images/ -> configure-agent
    """
    dir_name = image_dir.name
    if dir_name.endswith(".images"):
        return dir_name[: -len(".images")]
    return dir_name


def _resolve_exercise_slug(image_dir: Path) -> str:
    """Extract the exercise slug from the image directory path.

    Image dirs live under docs/<exercise-slug>/<step-slug>.images/
    """
    relative = image_dir.relative_to(DOCS_ROOT)
    parts = relative.parts
    if len(parts) >= 2:
        return parts[0]
    return ""


def _should_skip_dir(image_dir: Path) -> bool:
    """Check if this directory should be skipped."""
    relative = str(image_dir.relative_to(DOCS_ROOT))
    return any(relative.startswith(skip) or relative == skip for skip in SKIP_DIRS)


def scan_images(
    folder: Optional[Path] = None,
    force: bool = False,
    skip_assets: bool = True,
    single_image: Optional[Path] = None,
) -> list[ImageTask]:
    """Scan for images and return tasks for processing.

    Args:
        folder: Folder to scan. Defaults to DOCS_ROOT.
        force: If True, process images even if metadata exists.
        skip_assets: If True, skip docs/assets/images/.
        single_image: If set, process only this one image.

    Returns:
        List of ImageTask objects for images needing processing.
    """
    if single_image:
        path = Path(single_image).resolve()
        if not path.exists():
            print(f"Error: Image not found: {path}")
            return []
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            print(f"Error: Unsupported image type: {path.suffix}")
            return []
        metadata_path = path.with_suffix("").with_suffix(METADATA_SUFFIX)
        if metadata_path.exists() and not force:
            print(f"Skipping (metadata exists): {path.name}")
            return []
        return [
            ImageTask(
                image_path=path,
                metadata_path=metadata_path,
                lesson_slug=_resolve_lesson_slug(path.parent),
                exercise_slug=_resolve_exercise_slug(path.parent),
                image_name=path.name,
            )
        ]

    root = Path(folder).resolve() if folder else DOCS_ROOT
    if not root.exists():
        print(f"Error: Folder not found: {root}")
        return []

    tasks: list[ImageTask] = []
    skipped = 0

    for image_path in sorted(root.rglob("*")):
        if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if skip_assets and _should_skip_dir(image_path.parent):
            continue
        # Skip images inside site/ build output
        try:
            image_path.relative_to(DOCS_ROOT.parent / "site")
            continue
        except ValueError:
            pass

        metadata_path = image_path.with_suffix("").with_suffix(METADATA_SUFFIX)
        if metadata_path.exists() and not force:
            skipped += 1
            continue

        tasks.append(
            ImageTask(
                image_path=image_path,
                metadata_path=metadata_path,
                lesson_slug=_resolve_lesson_slug(image_path.parent),
                exercise_slug=_resolve_exercise_slug(image_path.parent),
                image_name=image_path.name,
            )
        )

    if skipped:
        print(f"Skipped {skipped} images with existing metadata (use --force to regenerate)")

    return tasks
