from pathlib import Path

# Folder containing files to rename
folder = Path("files_to_rename")

# New filename prefix
prefix = "file"

files = sorted([f for f in folder.iterdir() if f.is_file()])

for index, file in enumerate(files, start=1):
    new_name = f"{prefix}_{index}{file.suffix}"
    new_path = folder / new_name
    file.rename(new_path)

print(f"Renamed {len(files)} files.")