import os
import shutil
from datetime import datetime

# === USER CONFIGURATION ===
SOURCE_BASE = r"C:\Users\jay rathod\OneDrive\Pictures\Samsung Gallery"
DEST_BASE = r"C:\Photos of Phone\Samsung_Gallery"
VALID_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic', '.mp4', '.mov', '.avi', '.mkv']

# === FUNCTION TO MOVE FILES FROM ALBUM (INCLUDING SUBFOLDERS) ===
def move_files_from_album(album_name):
    today = datetime.today()
    month_folder = today.strftime("%Y-%m")
    source_album_path = os.path.join(SOURCE_BASE, album_name)
    dest_album_path = os.path.join(DEST_BASE, album_name, month_folder)

    if not os.path.isdir(source_album_path):
        print(f"Skipping {album_name} (not a folder)")
        return 0

    os.makedirs(dest_album_path, exist_ok=True)
    moved_count = 0

    for root, dirs, files in os.walk(source_album_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in VALID_EXTS:
                continue

            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_album_path, file)

            if os.path.exists(dest_file):
                print(f"Skipping (already exists): {file}")
                continue

            try:
                shutil.move(src_file, dest_file)
                moved_count += 1
                print(f"Moved: {file}")
            except Exception as e:
                print(f"Error moving {file}: {e}")

    return moved_count

# === MAIN FUNCTION TO PROCESS ALL ALBUMS ===
def run_conjo_transfer():
    print("Starting photo and video transfer process...")
    total_moved = 0

    for album_name in os.listdir(SOURCE_BASE):
        print(f"\nProcessing album: {album_name}")
        moved = move_files_from_album(album_name)
        total_moved += moved

    print(f"\nTotal files moved: {total_moved}")

    if total_moved > 0:
        print("All tasks completed successfully. Photos/videos moved and removed from OneDrive.")
    else:
        print("No new files found to move. Everything is already backed up.")

# === SCRIPT ENTRY POINT ===
if __name__ == "__main__":
    run_conjo_transfer()
