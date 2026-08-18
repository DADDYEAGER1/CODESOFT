import json
import re
from pathlib import Path

# ==========================================================
# CONFIG
# ==========================================================
CONTENT_DIR = Path(
    r"C:\Users\gaurav verma\mirelle baby\mirelle-site\src\content"
)

OUTPUT_DIR = Path(r"C:\Users\gaurav verma\scripts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "canonical_urls.txt"

# Folders to ignore
EXCLUDED_FOLDERS = {
    "inspo-images",
}

# Extra JSON file to include
INSPO_JSON = CONTENT_DIR / "inspo-categories.json"

SITE_URL = "https://mirellebeauty.com"

# ==========================================================
# Canonical regex
# ==========================================================
canonical_pattern = re.compile(
    r'^\s*canonical\s*:\s*["\']([^"\']+)["\']',
    re.MULTILINE,
)


# ==========================================================
# Get all available folders
# ==========================================================
folders = sorted(
    [
        f
        for f in CONTENT_DIR.iterdir()
        if f.is_dir() and f.name not in EXCLUDED_FOLDERS
    ],
    key=lambda x: x.name.lower(),
)

print("\nAvailable folders:\n")

for i, folder in enumerate(folders, start=1):
    print(f"{i}. {folder.name}")

print("\n0. ALL folders")

choice = input(
    "\nEnter folder numbers separated by commas (example: 1,3,5) or 0 for ALL: "
).strip()

# ==========================================================
# Determine folders
# ==========================================================
if choice == "0":
    selected_folders = folders
else:
    selected_folders = []

    for item in choice.split(","):
        item = item.strip()

        if not item.isdigit():
            continue

        idx = int(item)

        if 1 <= idx <= len(folders):
            selected_folders.append(folders[idx - 1])

# ==========================================================
# Collect canonicals
# ==========================================================
canonical_urls = []

for folder in selected_folders:

    print(f"\nScanning {folder.name}...")

    for file in folder.rglob("*"):

        if file.suffix.lower() not in {".md", ".mdx"}:
            continue

        try:
            content = file.read_text(encoding="utf-8")

            if not content.startswith("---"):
                continue

            parts = content.split("---", 2)

            if len(parts) < 3:
                continue

            frontmatter = parts[1]

            match = canonical_pattern.search(frontmatter)

            if match:
                canonical_urls.append(match.group(1))
            else:
                print(f"[WARNING] No canonical: {file.relative_to(CONTENT_DIR)}")

        except Exception as e:
            print(f"[ERROR] {file}: {e}")

# ==========================================================
# Include inspo-categories.json URLs
# ==========================================================
if INSPO_JSON.exists():

    print("\nScanning inspo-categories.json...")

    try:
        with open(INSPO_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)

        designs = data.get("designs", {})

        for design in designs.values():

            slug = design.get("slug")

            if slug:
                canonical_urls.append(f"{SITE_URL}/inspiration/{slug}/")

    except Exception as e:
        print(f"[ERROR] Reading inspo-categories.json: {e}")

# ==========================================================
# Remove duplicates & sort
# ==========================================================
canonical_urls = sorted(set(canonical_urls))

# ==========================================================
# Save
# ==========================================================
with OUTPUT_FILE.open("w", encoding="utf-8") as f:
    for url in canonical_urls:
        f.write(url + "\n")

# ==========================================================
# Summary
# ==========================================================
print("\n====================================")
print(f"Folders scanned : {len(selected_folders)}")
print(f"Canonical URLs  : {len(canonical_urls)}")
print(f"Saved to:\n{OUTPUT_FILE}")
print("====================================")