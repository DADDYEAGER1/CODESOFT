from pathlib import Path


def count_markdown_files(folder_path):
    # Remove surrounding quotes if present
    folder_path = folder_path.strip().strip('"').strip("'")

    path = Path(folder_path)

    if not path.exists():
        print(f"❌ Folder does not exist: {folder_path}")
        return 0

    if not path.is_dir():
        print(f"❌ Not a directory: {folder_path}")
        return 0

    count = 0
    for file in path.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".md", ".mdx"}:
            count += 1

    return count


def main():
    print("Enter folder paths (one per line).")
    print("Press Enter on an empty line when you're done.\n")

    folders = []

    while True:
        folder = input("Folder: ").strip()
        if folder == "":
            break
        folders.append(folder)

    if not folders:
        print("No folders entered.")
        return

    total = 0

    print("\nResults:")
    print("-" * 60)

    for folder in folders:
        cleaned = folder.strip().strip('"').strip("'")
        count = count_markdown_files(folder)
        total += count
        print(f"{cleaned}: {count} markdown file(s)")

    print("-" * 60)
    print(f"Total markdown (.md + .mdx) files across all folders: {total}")


if __name__ == "__main__":
    main()