import os
import json

def build_tree(path, skip_dirs=None, skip_exts=None, collapse_exts=None):
    """Recursively build a dictionary representing the folder structure."""
    if skip_dirs is None:
        skip_dirs = {"public", "node_modules", ".next", "dist", "turbo", "turbo-pack"}
    if skip_exts is None:
        skip_exts = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
    if collapse_exts is None:
        collapse_exts = {".md", ".mdx"}

    tree = {"name": os.path.basename(path)}

    if os.path.isdir(path):
        # Skip unwanted directories
        if os.path.basename(path).lower() in skip_dirs:
            return None

        tree["type"] = "directory"
        tree["children"] = []

        collapse_counts = {}

        for entry in os.listdir(path):
            # Skip hidden files/folders
            if entry.startswith("."):
                continue

            entry_path = os.path.join(path, entry)
            ext = os.path.splitext(entry)[1].lower()

            # Skip images
            if os.path.isfile(entry_path) and ext in skip_exts:
                continue

            # Collapse md/mdx into a count instead of listing each
            if os.path.isfile(entry_path) and ext in collapse_exts:
                collapse_counts[ext] = collapse_counts.get(ext, 0) + 1
                continue

            child = build_tree(entry_path, skip_dirs, skip_exts, collapse_exts)
            if child:
                tree["children"].append(child)

        for ext, count in collapse_counts.items():
            tree["children"].append({"name": f"{count} {ext} file(s)", "type": "summary"})
    else:
        tree["type"] = "file"

    return tree

if __name__ == "__main__":
    project_path = r"C:\Users\gaurav verma\mirelle baby\mirelle-site"
    output_json = "mirelle_tree.json"

    print(f"📂 Scanning project (excluding 'public' and build modules): {project_path}")
    tree_structure = build_tree(project_path)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(tree_structure, f, indent=4)

    print(f"✅ JSON tree saved to {output_json}")