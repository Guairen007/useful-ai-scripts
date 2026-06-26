from pathlib import Path
import shutil

# Change this path if needed
downloads = Path.home() / "Downloads"

# Map file extensions to folder names
folders = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images",
    ".pdf": "PDFs", ".docx": "Documents", ".txt": "Documents",
    ".mp4": "Videos", ".mov": "Videos",
    ".zip": "Archives", ".rar": "Archives"
}

for file in downloads.iterdir():
    if file.is_file():
        folder_name = folders.get(file.suffix.lower(), "Others")
        target_folder = downloads / folder_name
        target_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(target_folder / file.name))

print("Downloads folder organized.")