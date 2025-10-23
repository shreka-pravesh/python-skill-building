import os
def folder_stats(path):
    total_files = total_dirs = total_size = 0
    for root, dirs, files in os.walk(path):
        total_dirs += len(dirs)
        total_files += len(files)
        total_size += sum(os.path.getsize(os.path.join(root, f)) for f in files)
    print("\n Folder Summary Report:")
    print(f"Total Folders: {total_dirs}")
    print(f"Total Files  : {total_files}")
    print(f"Total Size   : {round(total_size / 1024, 2)} KB")
if __name__ == "__main__":
    folder_stats(input("Enter folder path: "))
