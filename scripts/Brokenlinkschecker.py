#!/usr/bin/env python3
"""
Broken Internal Link Checker (DRY RUN + APPLY mode)
====================================================
Scans .md / .mdx content files for internal <a href="..."> links,
compares them against a canonical list of valid URLs, and reports
any broken / mismatched links along with a best-guess correct match.

By default this script is READ-ONLY (dry run). It only writes a
report (CSV + Markdown + printed summary) and does not touch any
content files.

APPLY MODE (--apply):
    Only fixes classified as "Wrong route (slug match)" are applied
    automatically -- these are cases where a link's final URL slug is
    an exact, unique match to one canonical page, just filed under the
    wrong route/section. All other broken-link cases (year mismatches,
    typos, ambiguous matches, no-match, etc.) are left untouched for
    manual review.

    Before changing anything, every file that will be touched is
    backed up (preserving folder structure) into BACKUP_DIR.
    The terminal prints how many links will change and how many files
    are being backed up, BEFORE any file is modified.

    After applying fixes, the script automatically re-scans the
    (now partially fixed) content and writes a fresh CSV + Markdown
    report containing only the remaining, unfixed cases.

USAGE:
    python check_links.py            # dry run only, no files changed
    python check_links.py --apply    # apply slug-match fixes, then re-scan

CONFIGURE the variables in the CONFIG section below before running.
"""

import os
import re
import csv
import sys
import shutil
import difflib
from pathlib import Path
from urllib.parse import urlparse

# =========================== CONFIG =================================

# Your site's domain (used to recognize "internal" absolute links like
# https://yourdomain.com/some/path and to strip it when normalizing).
DOMAIN = "mirelleinspo.com"

# Path to the canonical URLs list (one URL per line).
CANONICAL_FILE = r"C:\Users\gaurav verma\scripts\canonical_urls.txt"

# Path to the content folder to scan recursively (.md and .mdx files).
CONTENT_DIR = r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content"

# Where to write the dry-run reports.
REPORT_CSV = "broken_links_report.csv"
REPORT_MD = "broken_links_report.md"

# Where backups of touched files go (before any edit in --apply mode).
# Folder structure of CONTENT_DIR is preserved underneath this folder.
BACKUP_DIR = "backup"

# Minimum similarity score (0-1) for a "best guess" suggestion to be
# shown. Below this, we just say "no close match found".
MIN_SUGGESTION_SCORE = 0.45

# Similarity score at/above which we consider it a confident "near typo".
HIGH_CONFIDENCE_SCORE = 0.85

# =====================================================================


def normalize_path(url_or_path: str) -> str:
    """
    Normalize a URL or path down to a comparable "slug path":
    - strips domain/scheme if present
    - strips query string and fragment
    - strips trailing slash
    - lowercases
    """
    if not url_or_path:
        return ""

    parsed = urlparse(url_or_path)

    if parsed.scheme or parsed.netloc:
        path = parsed.path
    else:
        # root-relative or relative path like "/blog/foo" or "blog/foo"
        path = url_or_path.split("?")[0].split("#")[0]

    path = path.strip()
    if not path.startswith("/"):
        path = "/" + path
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]

    return path.lower()


def load_canonicals(canonical_file: str):
    """
    Load canonical URLs, return:
      - canonical_lookup: dict normalized_path -> original_url
      - canonical_paths: list of normalized paths (for fuzzy matching)
    """
    canonical_lookup = {}
    with open(canonical_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            norm = normalize_path(line)
            canonical_lookup[norm] = line
    return canonical_lookup


def is_external_domain(href: str, domain: str) -> bool:
    """
    Return True if href points to a different domain (external link).
    Root-relative links (starting with /) are always internal.
    Protocol-relative / mailto / tel / anchor-only links are treated
    as "external / skip" (not something we correct against canonicals).
    """
    href = href.strip()

    if href.startswith("#"):
        return True  # pure anchor, not a page link
    if href.startswith("mailto:") or href.startswith("tel:"):
        return True
    if href.startswith("//"):
        # protocol-relative -- check host
        host = href[2:].split("/")[0].lower()
        return domain.lower() not in host
    if href.startswith("/"):
        return False  # root-relative -> internal

    parsed = urlparse(href)
    if parsed.netloc:
        return domain.lower() not in parsed.netloc.lower()

    # relative path without leading slash, e.g. "acrylic-nails/foo"
    return False


# Matches an entire <a ...>...</a> tag (non-greedy, dotall so it can
# span lines), capturing the opening tag attributes and inner text.
A_TAG_RE = re.compile(r"<a\s+([^>]*?)>(.*?)</a>", re.IGNORECASE | re.DOTALL)

# Matches an entire <img ... /> tag (self-closing or not), so we can
# strip these out before looking for links (images are never links,
# but this also guards against nested/adjacent weirdness).
IMG_TAG_RE = re.compile(r"<img\b[^>]*?/?>", re.IGNORECASE | re.DOTALL)

# Extract href='...' or href="..." from an attribute string.
HREF_RE = re.compile(r"""href\s*=\s*(['"])(.*?)\1""", re.IGNORECASE)


def find_links_in_text(text: str):
    """
    Yield (href, anchor_text, line_number) for every <a href="..."> in
    the given text, skipping any that live inside <img> tags (they
    won't match A_TAG_RE anyway since img tags aren't <a> tags -- this
    is mainly a safety net for malformed markup).
    """
    # Strip out img tags entirely first, just as a safety measure.
    text_no_img = IMG_TAG_RE.sub("", text)

    for match in A_TAG_RE.finditer(text_no_img):
        attrs, inner = match.group(1), match.group(2)
        href_match = HREF_RE.search(attrs)
        if not href_match:
            continue
        href = href_match.group(2)
        # anchor text: strip any nested tags for a clean label
        anchor_text = re.sub(r"<[^>]+>", "", inner).strip()
        line_number = text_no_img.count("\n", 0, match.start()) + 1
        yield href, anchor_text, line_number


def get_slug(norm_path: str) -> str:
    """
    Return the last non-empty path segment ("slug") of a normalized path.
    e.g. "/blog/work-nails" -> "work-nails"
         "/work-nails/work-nails" -> "work-nails"
    """
    parts = [p for p in norm_path.split("/") if p]
    return parts[-1] if parts else ""


def find_slug_match(norm_broken_path: str, canonical_paths):
    """
    Look for canonical URLs whose LAST path segment (slug) exactly
    matches the broken link's last path segment. Since slugs are
    expected to be unique across the whole site, a single match here
    is treated as a confirmed fix (not a fuzzy guess) -- e.g.
    "/blog/work-nails" matching canonical "/work-nails/work-nails"
    because "work-nails" is the same page slug, just filed under the
    wrong route.

    Returns:
      - (matched_path, True)  if exactly one canonical shares the slug
      - (None, False)         if zero or multiple canonicals share it
        (ambiguous or no match -- caller should fall back to fuzzy
        matching on the full path in either case)
    """
    slug = get_slug(norm_broken_path)
    if not slug:
        return None, False

    matches = [c for c in canonical_paths if get_slug(c) == slug]

    if len(matches) == 1:
        return matches[0], True

    return None, False  # zero or ambiguous (2+) -- fall back to fuzzy


def best_guess(norm_broken_path: str, canonical_paths):
    """
    Return (best_match_path, score) using difflib fuzzy matching
    against the list of canonical normalized paths.
    """
    if not canonical_paths:
        return None, 0.0

    matches = difflib.get_close_matches(
        norm_broken_path, canonical_paths, n=1, cutoff=0.0
    )
    if not matches:
        return None, 0.0

    best = matches[0]
    score = difflib.SequenceMatcher(None, norm_broken_path, best).ratio()
    return best, score


# Order matters: first matching rule wins.
CASE_SLUG_MATCH = "Wrong route (slug match)"
CASE_TRAILING_SLASH = "Trailing slash mismatch"
CASE_YEAR_NUMBER = "Wrong number / year in slug"
CASE_SECTION_PREFIX = "Wrong section (e.g. /blog/ vs /inspiration/)"
CASE_NEAR_TYPO = "Near typo / minor spelling difference"
CASE_MODERATE = "Moderate mismatch (needs manual review)"
CASE_NO_MATCH = "No close match found"


def classify_case(norm_broken: str, norm_guess: str, score: float) -> str:
    """
    Classify *why* a broken link is broken, so the markdown report can
    group similar issues together for faster human review.
    """
    if not norm_guess:
        return CASE_NO_MATCH

    # Trailing slash only difference (should be rare since we normalize
    # slashes already, but covers cases where everything else is identical
    # except normalize_path couldn't fully reconcile something odd).
    if norm_broken.rstrip("/") == norm_guess.rstrip("/") and norm_broken != norm_guess:
        return CASE_TRAILING_SLASH

    # Section prefix differs but the rest of the path (tail) matches.
    broken_parts = [p for p in norm_broken.split("/") if p]
    guess_parts = [p for p in norm_guess.split("/") if p]
    if (
        len(broken_parts) == len(guess_parts)
        and len(broken_parts) >= 2
        and broken_parts[0] != guess_parts[0]
        and broken_parts[1:] == guess_parts[1:]
    ):
        return CASE_SECTION_PREFIX

    # Same structure, but a number/year differs somewhere in the slug
    # (e.g. "2027" vs "2026", or "trends-2025" vs "trends-2026").
    broken_nums = re.findall(r"\d+", norm_broken)
    guess_nums = re.findall(r"\d+", norm_guess)
    broken_no_nums = re.sub(r"\d+", "#", norm_broken)
    guess_no_nums = re.sub(r"\d+", "#", norm_guess)
    if broken_nums != guess_nums and broken_no_nums == guess_no_nums:
        return CASE_YEAR_NUMBER

    if score >= HIGH_CONFIDENCE_SCORE:
        return CASE_NEAR_TYPO

    if score >= MIN_SUGGESTION_SCORE:
        return CASE_MODERATE

    return CASE_NO_MATCH


def scan_content(content_dir: str, domain: str, canonical_lookup: dict):
    """
    Walk content_dir for .md/.mdx files, extract internal links, and
    check each against canonical_lookup. Returns a list of result rows
    (dicts) -- one per internal link found (both OK and broken), so
    you get a full picture, plus a separate broken-only list.
    """
    canonical_paths = list(canonical_lookup.keys())
    all_rows = []
    broken_rows = []

    content_path = Path(content_dir)
    files = sorted(content_path.rglob("*.md")) + sorted(content_path.rglob("*.mdx"))

    for file_path in files:
        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  [WARN] Could not read {file_path}: {e}")
            continue

        for href, anchor_text, line_no in find_links_in_text(text):
            if is_external_domain(href, domain):
                continue  # skip external links, mailto, tel, pure anchors

            norm = normalize_path(href)

            is_ok = norm in canonical_lookup
            row = {
                "file": str(file_path.relative_to(content_path)),
                "line": line_no,
                "found_href": href,
                "anchor_text": anchor_text,
                "status": "OK" if is_ok else "BROKEN",
                "suggested_fix": "",
                "confidence": "",
                "case": "",
            }

            if not is_ok:
                # First, check for an exact unique slug match (e.g. the
                # link is filed under the wrong route/section, but its
                # last path segment matches exactly one canonical page).
                # This is treated as a confirmed fix, not a fuzzy guess.
                slug_match, is_unique = find_slug_match(norm, canonical_paths)

                if is_unique:
                    row["case"] = CASE_SLUG_MATCH
                    row["suggested_fix"] = canonical_lookup[slug_match]
                    row["confidence"] = "1.00"
                else:
                    # Zero or ambiguous (2+) slug matches -- fall back to
                    # the existing fuzzy-matching logic on the full path.
                    guess, score = best_guess(norm, canonical_paths)
                    case = classify_case(norm, guess, score)
                    row["case"] = case

                    if guess and score >= MIN_SUGGESTION_SCORE:
                        row["suggested_fix"] = canonical_lookup[guess]
                        row["confidence"] = f"{score:.2f}"
                    else:
                        row["suggested_fix"] = "(no close match found)"
                        row["confidence"] = f"{score:.2f}" if guess else "0.00"
                broken_rows.append(row)

            all_rows.append(row)

    return all_rows, broken_rows


# Preferred display order for case sections in the markdown report.
CASE_ORDER = [
    CASE_SLUG_MATCH,
    CASE_TRAILING_SLASH,
    CASE_YEAR_NUMBER,
    CASE_SECTION_PREFIX,
    CASE_NEAR_TYPO,
    CASE_MODERATE,
    CASE_NO_MATCH,
]

CASE_DESCRIPTIONS = {
    CASE_SLUG_MATCH: (
        "The link is filed under the wrong top-level route, but its final "
        "slug (the last part of the URL) is an exact, unique match for one "
        "canonical page. Since slugs are unique across the site, this is "
        "treated as a confirmed fix rather than a guess -- confidence 1.00."
    ),
    CASE_TRAILING_SLASH: (
        "The link matches a canonical URL exactly except for a missing or "
        "extra trailing slash. Safe, mechanical fix."
    ),
    CASE_YEAR_NUMBER: (
        "The link's slug is otherwise identical to a canonical URL but a "
        "number (often a year, e.g. 2027 vs 2026) differs. Likely an "
        "outdated year reference or simple typo -- verify the intended year "
        "before applying."
    ),
    CASE_SECTION_PREFIX: (
        "The link points to the wrong top-level section (e.g. /blog/ vs "
        "/inspiration/) but the rest of the path matches a canonical URL "
        "exactly. Likely the content moved to a different section."
    ),
    CASE_NEAR_TYPO: (
        f"High-confidence match (similarity >= {HIGH_CONFIDENCE_SCORE}) -- "
        "almost certainly a small spelling/formatting typo. Generally safe "
        "to apply, but do a quick visual check."
    ),
    CASE_MODERATE: (
        f"Medium-confidence match (similarity between {MIN_SUGGESTION_SCORE} "
        f"and {HIGH_CONFIDENCE_SCORE}). The suggested canonical is a "
        "plausible guess but not a strong one -- review manually before "
        "applying."
    ),
    CASE_NO_MATCH: (
        "No canonical URL was found that's even loosely similar to this "
        "link. This may be a page that no longer exists, was renamed "
        "beyond recognition, or was never a valid page. Needs manual "
        "investigation -- do not auto-apply."
    ),
}


def write_markdown_report(broken_rows, report_path: str, domain: str,
                           canonical_count: int, total_internal_links: int):
    """
    Write a human-readable Markdown report, grouping broken links by
    the *type* of mismatch (case), so a person can scan through each
    category and judge the suggested fixes in context.
    """
    grouped = {case: [] for case in CASE_ORDER}
    for row in broken_rows:
        grouped.setdefault(row["case"], []).append(row)

    lines = []
    lines.append("# Broken Internal Link Report (Dry Run)")
    lines.append("")
    lines.append(
        "This report was generated by a **read-only dry run**. "
        "No content files were modified."
    )
    lines.append("")
    lines.append(f"- Domain considered internal: `{domain}`")
    lines.append(f"- Canonical URLs loaded: **{canonical_count}**")
    lines.append(f"- Internal links scanned: **{total_internal_links}**")
    lines.append(f"- Broken internal links found: **{len(broken_rows)}**")
    lines.append("")
    lines.append("## Summary by case type")
    lines.append("")
    lines.append("| Case type | Count |")
    lines.append("|---|---|")
    for case in CASE_ORDER:
        count = len(grouped.get(case, []))
        if count:
            lines.append(f"| {case} | {count} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    for case in CASE_ORDER:
        rows = grouped.get(case, [])
        if not rows:
            continue

        lines.append(f"## {case} ({len(rows)})")
        lines.append("")
        lines.append(f"> {CASE_DESCRIPTIONS[case]}")
        lines.append("")

        for row in rows:
            lines.append(f"### `{row['file']}` (line {row['line']})")
            lines.append("")
            lines.append(f"- **Anchor text:** {row['anchor_text']!r}")
            lines.append(f"- **Found href:** `{row['found_href']}`")
            lines.append(f"- **Suggested fix:** `{row['suggested_fix']}`")
            lines.append(f"- **Confidence:** {row['confidence']}")
            lines.append(f"- **Approve this fix?** \u2610 yes &nbsp;&nbsp; \u2610 no &nbsp;&nbsp; \u2610 needs a different URL")
            lines.append("")

        lines.append("---")
        lines.append("")

    lines.append(
        "_Tip: fill in the checkboxes above (or just tell me the "
        "file names / cases you approve), and we'll build a second "
        "script that applies only the approved fixes -- with a backup "
        "of every file it touches before making changes._"
    )
    lines.append("")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def to_root_relative(canonical_url: str, domain: str) -> str:
    """
    Convert a canonical URL (which may be absolute, e.g.
    "https://mirelleinspo.com/work-nails/work-nails/") into a
    root-relative path (e.g. "/work-nails/work-nails/"), to match the
    site's existing root-relative link style. If it's already
    root-relative, it's returned unchanged (aside from whitespace).
    """
    canonical_url = canonical_url.strip()
    parsed = urlparse(canonical_url)

    if parsed.scheme or parsed.netloc:
        path = parsed.path or "/"
    else:
        path = canonical_url

    if not path.startswith("/"):
        path = "/" + path

    return path


def apply_slug_match_fixes(content_dir: str, domain: str, broken_rows,
                            backup_dir: str):
    """
    Apply fixes ONLY for rows classified as CASE_SLUG_MATCH (the
    "Wrong route (slug match)" case -- confirmed-safe fixes since each
    matched exactly one canonical page by unique slug).

    Before touching any file:
      1. Print how many links will change and how many files will be
         backed up.
      2. Copy every affected file into backup_dir, preserving its
         relative folder structure under content_dir.

    Then, for each affected file, replace the exact found href string
    (as it appeared in the source, single- or double-quoted) with the
    new root-relative path -- only within href="..." / href='...'
    attributes, so we never touch anchor text or other content.

    Returns a list of dicts describing exactly what changed, for the
    terminal summary.
    """
    content_path = Path(content_dir)
    backup_path = Path(backup_dir)

    slug_fix_rows = [r for r in broken_rows if r["case"] == CASE_SLUG_MATCH]

    if not slug_fix_rows:
        print("No 'Wrong route (slug match)' fixes to apply.\n")
        return []

    # Group fixes by file so we only read/write each file once.
    fixes_by_file = {}
    for row in slug_fix_rows:
        fixes_by_file.setdefault(row["file"], []).append(row)

    affected_files = sorted(fixes_by_file.keys())

    print("-" * 70)
    print("APPLY MODE -- 'Wrong route (slug match)' fixes only")
    print("-" * 70)
    print(f"Links to change:  {len(slug_fix_rows)}")
    print(f"Files to back up: {len(affected_files)}")
    for fname in affected_files:
        print(f"  - {fname}")
    print()

    # --- Step 1: back up every affected file BEFORE editing anything ---
    for fname in affected_files:
        src = content_path / fname
        dst = backup_path / fname
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    print(f"Backed up {len(affected_files)} file(s) to: {backup_path.resolve()}\n")

    # --- Step 2: apply the fixes ---
    changes = []
    for fname, rows in fixes_by_file.items():
        file_path = content_path / fname
        text = file_path.read_text(encoding="utf-8")
        original_text = text

        for row in rows:
            found_href = row["found_href"]
            new_href = to_root_relative(row["suggested_fix"], domain)

            # Replace href="found_href" or href='found_href' with the
            # new href, preserving whichever quote style was used.
            # Only the href value changes -- nothing else in the tag.
            pattern = re.compile(
                r"""(href\s*=\s*)(['"])""" + re.escape(found_href) + r"""\2""",
                re.IGNORECASE,
            )

            def _replacement(m, new_href=new_href):
                quote = m.group(2)
                return f"{m.group(1)}{quote}{new_href}{quote}"

            text, count = pattern.subn(_replacement, text)

            changes.append({
                "file": fname,
                "line": row["line"],
                "old_href": found_href,
                "new_href": new_href,
                "replacements_made": count,
            })

        if text != original_text:
            file_path.write_text(text, encoding="utf-8")

    print("-" * 70)
    print("CHANGES APPLIED:")
    print("-" * 70)
    for c in changes:
        status = "OK" if c["replacements_made"] > 0 else "NOT FOUND (skipped)"
        print(f"\nFile:     {c['file']} (line {c['line']})")
        print(f"Old href: {c['old_href']}")
        print(f"New href: {c['new_href']}")
        print(f"Status:   {status}")

    applied_count = sum(1 for c in changes if c["replacements_made"] > 0)
    print(f"\n{applied_count} of {len(changes)} link(s) successfully updated.\n")

    return changes


def main():
    apply_mode = "--apply" in sys.argv

    print("=" * 70)
    if apply_mode:
        print("BROKEN INTERNAL LINK CHECKER -- APPLY MODE")
        print("(slug-match fixes will be written to disk; backups made first)")
    else:
        print("BROKEN INTERNAL LINK CHECKER -- DRY RUN (no files will be changed)")
    print("=" * 70)

    print(f"\nDomain considered 'internal': {DOMAIN}")
    print(f"Canonical file: {CANONICAL_FILE}")
    print(f"Content directory: {CONTENT_DIR}\n")

    if not os.path.exists(CANONICAL_FILE):
        print(f"[ERROR] Canonical file not found: {CANONICAL_FILE}")
        return
    if not os.path.exists(CONTENT_DIR):
        print(f"[ERROR] Content directory not found: {CONTENT_DIR}")
        return

    canonical_lookup = load_canonicals(CANONICAL_FILE)
    print(f"Loaded {len(canonical_lookup)} canonical URLs.\n")

    all_rows, broken_rows = scan_content(CONTENT_DIR, DOMAIN, canonical_lookup)

    total_internal_links = len(all_rows)
    total_broken = len(broken_rows)
    total_files_with_broken = len({r["file"] for r in broken_rows})

    print(f"Scanned internal links found: {total_internal_links}")
    print(f"Broken internal links found:  {total_broken}")
    print(f"Files containing broken links: {total_files_with_broken}\n")

    if broken_rows:
        print("-" * 70)
        print("BROKEN LINKS (with best-guess correct canonical):")
        print("-" * 70)
        for row in broken_rows:
            print(f"\nFile:        {row['file']} (line {row['line']})")
            print(f"Anchor text: {row['anchor_text']!r}")
            print(f"Found href:  {row['found_href']}")
            print(f"Suggested:   {row['suggested_fix']}  (confidence: {row['confidence']})")

    # Write full CSV report (broken links only, since that's the actionable list)
    with open(REPORT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["file", "line", "found_href", "anchor_text",
                        "status", "suggested_fix", "confidence", "case"],
        )
        writer.writeheader()
        for row in broken_rows:
            writer.writerow(row)

    # Write the human-readable markdown report, grouped by case type.
    write_markdown_report(
        broken_rows,
        REPORT_MD,
        DOMAIN,
        canonical_count=len(canonical_lookup),
        total_internal_links=total_internal_links,
    )

    print(f"\n\nDry-run CSV report written to: {REPORT_CSV}")
    print(f"Dry-run Markdown report written to: {REPORT_MD}")
    print("No content files were modified. Review the reports, then we can")
    print("build a second script to apply the approved fixes.")


if __name__ == "__main__":
    main()