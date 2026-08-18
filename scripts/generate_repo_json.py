import os
import json

# ========================
# FILES TO EXPORT
# ========================
files_to_include = [
"src/app/stories/[slug]/page.tsx",
"src/types/stories.ts",
]


# ========================
# PROJECT ROOT PATH
# ========================
project_path = r"C:\Users\gaurav verma\mirelle baby\mirelle-site"

# ========================
# OUTPUT FILE
# ========================
output_file = r"C:\Users\gaurav verma\scripts\exported files.json"

# ========================
# ENSURE OUTPUT FOLDER EXISTS
# ========================
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# ========================
# SAFE FILE READER
# ========================
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return {
            "error": str(e),
            "path": path
        }

# ========================
# COLLECT FILE CONTENTS
# ========================
export_data = []
missing_files = []

for file_path in files_to_include:
    full_path = os.path.join(project_path, file_path.replace("/", os.sep))

    if os.path.exists(full_path):
        export_data.append({
            "path": file_path,
            "content": read_file(full_path)
        })
    else:
        missing_files.append(file_path)

# ========================
# WRITE OUTPUT JSON
# ========================
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(
        {
            "context": "Exported project files",
            "files": export_data,
            "missing": missing_files
        },
        f,
        indent=2,
        ensure_ascii=False
    )

# ========================
# SUMMARY
# ========================
print("✅ File exported")
print(f"📄 Output file: {output_file}")
print(f"📦 Files exported: {len(export_data)}")

if missing_files:
    print("\n⚠️ Missing files:")
    for m in missing_files:
        print(" -", m)