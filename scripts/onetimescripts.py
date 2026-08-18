#!/usr/bin/env python3
"""
Updates image path references from /images/blog/japanese-nails/
to /images/blog/japanese-nails-v1/ across:
  1. All .md files in the blogs/japanese-nails folder (frontmatter + body <img> tags)
  2. The inspo-images JSON gallery file

Does NOT rename folders/files on disk. Does NOT touch `id` fields.
Only replaces the exact path segment /images/blog/japanese-nails/
so it won't false-match on ids like "japanese-nails-001" or alt text.

Usage:
  python update_image_paths.py --dry-run     # preview changes, no writes
  python update_image_paths.py --apply       # actually write changes
"""

import argparse
import re
import sys
from pathlib import Path

# ---- CONFIG: adjust these two paths if your layout differs ----
MD_FOLDER = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content\blogs\japanese-nails")
JSON_FILE = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content\inspo-images\japanese-nails-inspiration-gallery.json")

OLD_SEGMENT = "/images/blog/japanese-nails/"
NEW_SEGMENT = "/images/blog/japanese-nails-v1/"


def find_occurrences(text: str) -> list[str]:
    """Return the lines containing the old path segment, for preview."""
    return [line for line in text.splitlines() if OLD_SEGMENT in line]


def process_file(path: Path, apply: bool) -> int:
    """Returns count of replacements made (or that would be made)."""
    original = path.read_text(encoding="utf-8")
    count = original.count(OLD_SEGMENT)
    if count == 0:
        return 0

    print(f"\n--- {path.relative_to(path.anchor) if path.is_absolute() else path} ---")
    for line in find_occurrences(original):
        stripped = line.strip()
        new_line = stripped.replace(OLD_SEGMENT, NEW_SEGMENT)
        print(f"  - {stripped}")
        print(f"  + {new_line}")

    if apply:
        updated = original.replace(OLD_SEGMENT, NEW_SEGMENT)
        path.write_text(updated, encoding="utf-8")

    return count


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="Preview changes only")
    group.add_argument("--apply", action="store_true", help="Write changes to disk")
    args = parser.parse_args()

    apply = args.apply

    if not MD_FOLDER.exists():
        print(f"ERROR: MD folder not found: {MD_FOLDER}")
        sys.exit(1)
    if not JSON_FILE.exists():
        print(f"ERROR: JSON file not found: {JSON_FILE}")
        sys.exit(1)

    md_files = sorted(MD_FOLDER.rglob("*.md"))
    if not md_files:
        print(f"WARNING: No .md files found under {MD_FOLDER}")

    total_files_changed = 0
    total_replacements = 0

    print(f"Mode: {'APPLY (writing changes)' if apply else 'DRY RUN (no changes written)'}")
    print(f"Replacing: {OLD_SEGMENT}  ->  {NEW_SEGMENT}")

    for md_file in md_files:
        n = process_file(md_file, apply)
        if n:
            total_files_changed += 1
            total_replacements += n

    n = process_file(JSON_FILE, apply)
    if n:
        total_files_changed += 1
        total_replacements += n

    print("\n" + "=" * 50)
    print(f"Files with matches: {total_files_changed}")
    print(f"Total replacements: {total_replacements}")
    if not apply:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Re-run with --apply to write changes.")
    else:
        print("\nChanges written.")


if __name__ == "__main__":
    main()