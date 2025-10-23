import zipfile, os
def create_archive(source, output):
    with zipfile.ZipFile(output, "w") as zf:
        for root, _, files in os.walk(source):
            for file in files:
                zf.write(os.path.join(root, file),
                         os.path.relpath(os.path.join(root, file), source))
    print(f" Archive {output} created successfully!")
def extract_archive(zip_path, dest):
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(dest)
    print(f" Extracted to {dest}")
if __name__ == "__main__":
    choice = input("Create (C) or Extract (E) archive? ").lower()
    if choice == 'c':
        create_archive(input("Source folder: "), input("Output zip name: "))
    else:
        extract_archive(input("Zip file: "), input("Destination folder: "))
