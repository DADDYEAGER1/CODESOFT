#!/usr/bin/env python3
"""
Auto-generate missing inspo-gallery image JSONs.

No input args. Fully hardcoded paths, runs end-to-end:

  1. Scan BLOGS_DIR's immediate subfolders.
  2. A subfolder is "eligible" if ANY .md file inside it has
     frontmatter: showInspoGalleryLink: true
  3. For each eligible folder, check INSPO_DIR for a file named
     "<folder>-inspiration-gallery.json".
     - If it EXISTS -> skip (already has a gallery).
     - If MISSING   -> extract images (frontmatter + body <img> tags)
                       from every .md in that folder and write
                       "<folder>-inspiration-gallery.json" to OUTPUT_DIR.

Usage:
  python generate_inspo_images.py
"""

import re
import json
from pathlib import Path

BLOGS_DIR = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content\blogs")
INSPO_DIR = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content\inspo-images")
OUTPUT_DIR = Path(r"C:\Users\gaurav verma\Downloads\images json")

# --- Frontmatter regexes -----------------------------------------------
FRONTMATTER_BLOCK_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)
FM_IMAGE_RE = re.compile(r"""^\s*image\s*:\s*["'](?P<val>.*?)["']\s*$""", re.MULTILINE)
FM_IMAGE_ALT_RE = re.compile(r"""^\s*imageAlt\s*:\s*["'](?P<val>.*?)["']\s*$""", re.MULTILINE)
FM_GALLERY_FLAG_RE = re.compile(
    r"""^\s*showInspoGalleryLink\s*:\s*(?P<val>true|false)\s*$""",
    re.MULTILINE | re.IGNORECASE,
)

# --- Body <img> regex ----------------------------------------------------
IMG_TAG_RE = re.compile(r"<img\b[^>]*?/?>", re.IGNORECASE | re.DOTALL)
ATTR_SRC_RE = re.compile(r"""\bsrc\s*=\s*["'](?P<val>.*?)["']""", re.IGNORECASE | re.DOTALL)
ATTR_ALT_RE = re.compile(r"""\balt\s*=\s*["'](?P<val>.*?)["']""", re.IGNORECASE | re.DOTALL)


def get_frontmatter_block(text):
    m = FRONTMATTER_BLOCK_RE.match(text)
    return m.group(1) if m else None


def has_gallery_flag_true(text):
    block = get_frontmatter_block(text)
    if block is None:
        return False
    m = FM_GALLERY_FLAG_RE.search(block)
    return bool(m) and m.group("val").lower() == "true"


def extract_frontmatter_image(text):
    block = get_frontmatter_block(text)
    if block is None:
        return None, None
    img_m = FM_IMAGE_RE.search(block)
    alt_m = FM_IMAGE_ALT_RE.search(block)
    image = img_m.group("val").strip() if img_m else None
    image_alt = alt_m.group("val").strip() if alt_m else None
    return image, image_alt


def extract_body_images(text):
    body = FRONTMATTER_BLOCK_RE.sub("", text, count=1)
    results = []
    for tag_match in IMG_TAG_RE.finditer(body):
        tag = tag_match.group(0)
        src_m = ATTR_SRC_RE.search(tag)
        alt_m = ATTR_ALT_RE.search(tag)
        results.append({
            "image": src_m.group("val").strip() if src_m else None,
            "imageAlt": alt_m.group("val").strip() if alt_m else None,
        })
    return results


def process_file(path: Path):
    text = path.read_text(encoding="utf-8")
    fm_image, fm_alt = extract_frontmatter_image(text)
    body_images = extract_body_images(text)
    return {
        "file": path.name,
        "frontmatter": {
            "image": fm_image,
            "imageAlt": fm_alt,
        },
        "body_images": body_images,
    }


def find_eligible_folders(blogs_dir: Path):
    """Return sorted list of immediate subfolders containing >=1 md file
    with showInspoGalleryLink: true."""
    eligible = []
    if not blogs_dir.is_dir():
        print(f"[error] blogs dir not found: {blogs_dir}")
        return eligible

    for sub in sorted(p for p in blogs_dir.iterdir() if p.is_dir()):
        md_files = list(sub.glob("*.md"))
        flagged = False
        for f in md_files:
            try:
                text = f.read_text(encoding="utf-8")
            except Exception as e:
                print(f"  [error] reading {f}: {e}")
                continue
            if has_gallery_flag_true(text):
                flagged = True
                break
        if flagged:
            eligible.append(sub)

    return eligible


def existing_gallery_names(inspo_dir: Path):
    """Return set of folder-name prefixes that already have a
    <name>-inspiration-gallery.json file in inspo_dir."""
    existing = set()
    if not inspo_dir.is_dir():
        print(f"[warn] inspo-images dir not found: {inspo_dir}")
        return existing

    suffix = "-inspiration-gallery.json"
    for f in inspo_dir.glob(f"*{suffix}"):
        name = f.name[: -len(suffix)]
        existing.add(name)

    return existing


def main():
    print(f"Scanning blogs dir: {BLOGS_DIR}")
    eligible_folders = find_eligible_folders(BLOGS_DIR)
    print(f"Eligible folders (showInspoGalleryLink: true): {len(eligible_folders)}")
    for f in eligible_folders:
        print(f"  - {f.name}")

    print(f"\nChecking existing galleries in: {INSPO_DIR}")
    existing = existing_gallery_names(INSPO_DIR)
    print(f"Existing gallery JSONs found: {len(existing)}")

    missing_folders = [f for f in eligible_folders if f.name not in existing]

    print(f"\nFolders missing a gallery JSON: {len(missing_folders)}")
    for f in missing_folders:
        print(f"  - {f.name}")

    if not missing_folders:
        print("\nNothing to generate. Done.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating JSONs into: {OUTPUT_DIR}")
    for folder in missing_folders:
        md_files = sorted(folder.glob("*.md"))
        entries = []
        for f in md_files:
            try:
                entries.append(process_file(f))
            except Exception as e:
                print(f"  [error] failed on {f}: {e}")

        out_path = OUTPUT_DIR / f"{folder.name}-inspiration-gallery.json"
        with out_path.open("w", encoding="utf-8") as fh:
            json.dump(entries, fh, indent=2, ensure_ascii=False)

        print(f"  -> {folder.name}: {len(entries)} files -> {out_path.name}")

    print("\nDone.")


if __name__ == "__main__":
    main()