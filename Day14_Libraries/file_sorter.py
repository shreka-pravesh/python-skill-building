import os, shutil
def file_sorter():
    print("=== File Sorter ===")
    folders = {'Images': ['.jpg', '.png', '.jpeg'],
               'Docs': ['.txt', '.pdf', '.docx'],
               'Code': ['.py', '.c', '.cpp', '.js']}
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
    for file in os.listdir('.'):
        name, ext = os.path.splitext(file)
        for folder, exts in folders.items():
            if ext.lower() in exts:
                shutil.move(file, os.path.join(folder, file))
                print(f"Moved {file} → {folder}")
                break
    print("Files organized successfully!")
if __name__ == "__main__":
    file_sorter()
