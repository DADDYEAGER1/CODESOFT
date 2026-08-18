#!/usr/bin/env python3
"""
Fix canonical URLs in frontmatter to match the expected URL derived from file path.

Same detection logic as check_canonicals.py, but this one WRITES the fix
back into the file's frontmatter.

Safety:
  - Defaults to DRY RUN. No files are touched unless you pass --apply.
  - When --apply is used, every file that gets changed is first backed up
    to BACKUP_DIR (mirrors the original folder structure) before being
    overwritten.
  - Files with a MISSING canonical are left alone (skipped, not fixed) -
    same as agreed, since those need manual review.

Usage:
  python fix_canonicals.py            # dry run - shows what WOULD change
  python fix_canonicals.py --apply    # actually rewrites the files (with backup)
"""

import re
import sys
import shutil
from pathlib import Path
from datetime import datetime

BASE = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content")
DOMAIN = "https://mirelleinspo.com"
BACKUP_DIR = Path(r"C:\Users\gaurav verma\Downloads\canonical-backups") / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

FOLDER_URL_PREFIX = {
    "blogs": "blog",
    "business": "business",
    "faqs": "nail-faqs",
    "pinterest": "pinterest",
    "reports": "trend-reports",
    "shop": "shop",
    "spotlights": "spotlight",
    "topics": "topics",
    "work-nails": "work-nails",
}

FRONTMATTER_BLOCK_RE = re.compile(r"^(---\s*\n)(.*?\n)(---\s*\n)", re.DOTALL)
FM_CANONICAL_LINE_RE = re.compile(r"""^(\s*canonical\s*:\s*)(["'])(.*?)\2(\s*)$""", re.MULTILINE)


def find_content_files(folder_root: Path):
    return sorted(list(folder_root.rglob("*.md")) + list(folder_root.rglob("*.mdx")))


def get_frontmatter_match(text):
    return FRONTMATTER_BLOCK_RE.match(text)


def extract_canonical(fm_block_text):
    m = FM_CANONICAL_LINE_RE.search(fm_block_text)
    return m.group(3).strip() if m else None


def expected_canonical(folder_root: Path, file_path: Path, url_prefix: str):
    rel = file_path.relative_to(folder_root).with_suffix("")
    return f"{DOMAIN}/{url_prefix}/{rel.as_posix()}"


def rewrite_canonical(full_text, new_canonical):
    """Replace the canonical line's value in-place, preserving quote style
    and everything else in the file byte-for-byte."""
    def _sub(m):
        prefix, quote, _old_val, trailing = m.group(1), m.group(2), m.group(3), m.group(4)
        return f"{prefix}{quote}{new_canonical}{quote}{trailing}"
    new_text, count = FM_CANONICAL_LINE_RE.subn(_sub, full_text, count=1)
    return new_text, count == 1


def backup_file(file_path: Path):
    rel = file_path.relative_to(BASE)
    dest = BACKUP_DIR / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, dest)


def process_folder(folder_name: str, url_prefix: str, apply: bool):
    folder_root = BASE / folder_name
    if not folder_root.is_dir():
        print(f"[skip] folder not found: {folder_root}")
        return {"fixed": 0, "skipped_missing": 0, "already_ok": 0, "errors": 0}

    stats = {"fixed": 0, "skipped_missing": 0, "already_ok": 0, "errors": 0}

    for file_path in find_content_files(folder_root):
        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  [error] reading {file_path}: {e}")
            stats["errors"] += 1
            continue

        fm_match = get_frontmatter_match(text)
        if not fm_match:
            continue  # no frontmatter at all - nothing to fix

        fm_block = fm_match.group(2)
        actual = extract_canonical(fm_block)
        expected = expected_canonical(folder_root, file_path, url_prefix)

        if actual is None:
            stats["skipped_missing"] += 1
            continue  # missing canonical - leave for manual review, per agreement

        if actual == expected:
            stats["already_ok"] += 1
            continue

        # Mismatch found - fix it
        print(f"{file_path}")
        print(f"    old: {actual}")
        print(f"    new: {expected}")

        if apply:
            new_text, ok = rewrite_canonical(text, expected)
            if not ok:
                print(f"    [error] could not locate canonical line to rewrite - skipped")
                stats["errors"] += 1
                continue
            backup_file(file_path)
            file_path.write_text(new_text, encoding="utf-8")
            print(f"    [fixed]")
        else:
            print(f"    [dry-run - not written]")

        stats["fixed"] += 1
        print()

    return stats


def main():
    apply = "--apply" in sys.argv

    if apply:
        print(f"APPLY MODE - files will be rewritten. Backups -> {BACKUP_DIR}\n")
    else:
        print("DRY RUN - no files will be changed. Re-run with --apply to write fixes.\n")

    totals = {"fixed": 0, "skipped_missing": 0, "already_ok": 0, "errors": 0}

    for folder_name, url_prefix in FOLDER_URL_PREFIX.items():
        stats = process_folder(folder_name, url_prefix, apply)
        for k in totals:
            totals[k] += stats[k]

    print("=" * 60)
    print(f"{'Fixed' if apply else 'Would fix'}: {totals['fixed']}")
    print(f"Already correct: {totals['already_ok']}")
    print(f"Skipped (missing canonical, needs manual review): {totals['skipped_missing']}")
    print(f"Errors: {totals['errors']}")
    if apply and totals["fixed"] > 0:
        print(f"\nBackups saved to: {BACKUP_DIR}")


if __name__ == "__main__":
    main()