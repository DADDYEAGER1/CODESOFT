"""
check_broken_images.py

Purpose:
    READ-ONLY CHECK. Does not modify any file.

    Recursively scans every .md and .mdx file under the content folder,
    extracts every image reference (both the frontmatter "image:" field and
    any <img src="..."> tags in the body), and checks each one against the
    public images folder (the source of truth). Reports which references
    are valid (file exists) and which are broken (file does not exist),
    grouped by the .md/.mdx file they were found in.

    This script makes NO changes anywhere. It's purely a report so you can
    see the scope of the problem before deciding what to fix.

Usage:
    python check_broken_images.py

    Optionally write the full report to a text file as well as printing it:
        python check_broken_images.py --report-file broken_images_report.txt
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# HARDCODED PATHS - edit these to match your machine
# ---------------------------------------------------------------------------

# Root of the content folder to scan recursively for .md / .mdx files
CONTENT_DIR = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content")

# Root of the public folder. Image paths like "/images/blog/foo/bar.webp"
# resolve to PUBLIC_ROOT/images/blog/foo/bar.webp
PUBLIC_ROOT = Path(r"C:\Users\gaurav verma\mirelle baby\mirelle-site\public")

# ---------------------------------------------------------------------------

# Matches image paths starting with /images/ up to the closing quote.
# Covers both:
#   image: "/images/blog/.../foo.webp"
#   src='/images/blog/.../foo.webp'  or  src="/images/blog/.../foo.webp"
IMAGE_PATH_PATTERN = re.compile(r"/images/[^\"'\s)]+\.(?:webp|png|jpe?g|gif|svg|avif)", re.IGNORECASE)


def find_content_files(content_dir: Path) -> list[Path]:
    """Recursively find every .md and .mdx file under content_dir."""
    if not content_dir.is_dir():
        print(f"ERROR: content folder does not exist: {content_dir}")
        sys.exit(1)
    files = sorted(list(content_dir.rglob("*.md")) + list(content_dir.rglob("*.mdx")))
    if not files:
        print(f"ERROR: no .md or .mdx files found under {content_dir}")
        sys.exit(1)
    return files


def extract_image_paths(text: str) -> list[str]:
    """Return unique /images/... paths found in text, in first-seen order."""
    seen = []
    for match in IMAGE_PATH_PATTERN.findall(text):
        if match not in seen:
            seen.append(match)
    return seen


def image_path_to_disk_path(image_path: str, public_root: Path) -> Path:
    """Convert a web path like /images/blog/foo/bar.webp into an actual filesystem path."""
    return public_root.joinpath(*image_path.strip("/").split("/"))


def main():
    report_lines: list[str] = []

    def out(line: str = ""):
        print(line)
        report_lines.append(line)

    report_file = None
    if "--report-file" in sys.argv:
        idx = sys.argv.index("--report-file")
        if idx + 1 < len(sys.argv):
            report_file = Path(sys.argv[idx + 1])

    out("=" * 70)
    out("check_broken_images.py  (READ-ONLY - no files will be modified)")
    out(f"Content folder : {CONTENT_DIR}")
    out(f"Public folder  : {PUBLIC_ROOT}")
    out("=" * 70)

    if not PUBLIC_ROOT.is_dir():
        print(f"ERROR: public folder does not exist: {PUBLIC_ROOT}")
        sys.exit(1)

    content_files = find_content_files(CONTENT_DIR)
    out(f"\nFound {len(content_files)} .md/.mdx file(s) under {CONTENT_DIR}")

    total_refs = 0
    total_valid = 0
    total_broken = 0
    files_with_broken: list[tuple[Path, list[str]]] = []
    files_with_no_images = 0

    out("\n--- Scanning files ---")
    for f in content_files:
        text = f.read_text(encoding="utf-8")
        image_paths = extract_image_paths(text)

        if not image_paths:
            files_with_no_images += 1
            continue

        broken_in_this_file = []
        valid_in_this_file = 0

        for img_path in image_paths:
            disk_path = image_path_to_disk_path(img_path, PUBLIC_ROOT)
            total_refs += 1
            if disk_path.is_file():
                total_valid += 1
                valid_in_this_file += 1
            else:
                total_broken += 1
                broken_in_this_file.append(img_path)

        rel = f.relative_to(CONTENT_DIR)
        if broken_in_this_file:
            out(f"\n  [{rel}]")
            out(f"    {valid_in_this_file} valid, {len(broken_in_this_file)} BROKEN:")
            for bp in broken_in_this_file:
                out(f"      - {bp}")
            files_with_broken.append((f, broken_in_this_file))
        # Files with all-valid images are not printed individually to keep
        # the output focused on problems; they're still counted in totals.

    out("\n" + "=" * 70)
    out("SUMMARY")
    out(f"  .md/.mdx files scanned          : {len(content_files)}")
    out(f"  files with no image references  : {files_with_no_images}")
    out(f"  files with at least one broken  : {len(files_with_broken)}")
    out(f"  total image references found    : {total_refs}")
    out(f"  valid (file exists)             : {total_valid}")
    out(f"  BROKEN (file does not exist)    : {total_broken}")
    out("=" * 70)

    if files_with_broken:
        out("\nFiles with broken images (path relative to content folder):")
        for f, broken_list in files_with_broken:
            rel = f.relative_to(CONTENT_DIR)
            out(f"  {rel}  ({len(broken_list)} broken)")
    else:
        out("\nNo broken images found. Everything referenced in .md/.mdx matches a file in public.")

    if report_file:
        report_file.write_text("\n".join(report_lines), encoding="utf-8")
        print(f"\nFull report also written to: {report_file}")


if __name__ == "__main__":
    main()