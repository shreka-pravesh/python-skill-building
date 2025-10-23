import os, shutil, logging
from datetime import datetime
def organize(folder, backup_dir):
    log_file = os.path.join(folder, "organizer.log")
    logging.basicConfig(filename=log_file, level=logging.INFO)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            ext = os.path.splitext(file)[1].lower()
            category = ext[1:] if ext else "others"
            dest_folder = os.path.join(folder, category)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(path, dest_folder)
            backup_path = os.path.join(backup_dir, f"{file}_{datetime.now().strftime('%Y%m%d%H%M%S')}")
            shutil.copy2(os.path.join(dest_folder, file), backup_path)
            logging.info(f"Moved {file} to {category}/ and backed up at {backup_path}")
    print(" Organization and backup complete. Log saved!")
if __name__ == "__main__":
    organize(input("Enter main folder path: "), input("Enter backup folder path: "))
