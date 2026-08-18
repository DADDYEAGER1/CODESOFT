import json
from pathlib import Path


def count_images(data):
    total = 0

    def traverse(obj):
        nonlocal total

        if isinstance(obj, dict):
            # Count hero image if present and non-empty
            if obj.get("hero_image"):
                total += 1

            # Count body images
            if isinstance(obj.get("body_images"), list):
                total += len(obj["body_images"])

            # Recurse into nested dictionaries/lists
            for value in obj.values():
                traverse(value)

        elif isinstance(obj, list):
            for item in obj:
                traverse(item)

    traverse(data)
    return total


def process_json(file_path):
    file_path = file_path.strip().strip('"').strip("'")
    path = Path(file_path)

    if not path.exists():
        print(f"❌ File not found: {file_path}")
        return 0

    if path.suffix.lower() != ".json":
        print(f"❌ Not a JSON file: {file_path}")
        return 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return count_images(data)

    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return 0


def main():
    print("Enter JSON file paths (one per line).")
    print("Press Enter on an empty line when you're done.\n")

    files = []

    while True:
        file = input("JSON File: ").strip()
        if file == "":
            break
        files.append(file)

    if not files:
        print("No files entered.")
        return

    grand_total = 0

    print("\nResults:")
    print("-" * 70)

    for file in files:
        cleaned = file.strip().strip('"').strip("'")
        count = process_json(file)
        grand_total += count
        print(f"{cleaned}: {count} image(s)")

    print("-" * 70)
    print(f"Total images across all JSON files: {grand_total}")


if __name__ == "__main__":
    main()