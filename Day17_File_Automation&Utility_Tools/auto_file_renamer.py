import os
from datetime import datetime
def bulk_rename(path, prefix):
    if not os.path.exists(path):
        print(" Folder not found.")
        return
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if not files:
        print("No files to rename.")
        return
    date_tag = datetime.now().strftime("%Y%m%d")
    for i, file in enumerate(files, start=1):
        name, ext = os.path.splitext(file)
        new_name = f"{prefix}_{date_tag}_{i}{ext}"
        os.rename(os.path.join(path, file), os.path.join(path, new_name))
    print(f" {len(files)} files renamed successfully!")
if __name__ == "__main__":
    folder = input("Enter directory path: ")
    prefix = input("Enter prefix for files: ")
    bulk_rename(folder, prefix)
