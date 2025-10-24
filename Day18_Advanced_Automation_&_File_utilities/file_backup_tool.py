import os
import shutil
from datetime import datetime
def create_backup(src_folder):
    if not os.path.exists(src_folder):
        print(" Source folder not found!")
        return
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
    shutil.copytree(src_folder, backup_path)
    print(f"\n Backup created at: {backup_path}\n")
    file_count = sum(len(files) for _, _, files in os.walk(src_folder))
    print(f"Total files backed up: {file_count}")
if __name__ == "__main__":
    folder = input("Enter the folder path to back up: ")
    create_backup(folder)
