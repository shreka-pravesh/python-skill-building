import os, csv
from datetime import datetime
def extract_metadata(folder, output):
    with open(output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Filename", "Size (KB)", "Modified", "Type"])
        for file in os.listdir(folder):
            path = os.path.join(folder, file)
            if os.path.isfile(path):
                size = round(os.path.getsize(path) / 1024, 2)
                mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")
                ext = os.path.splitext(file)[1] or "N/A"
                writer.writerow([file, size, mtime, ext])
    print(f" Metadata exported to {output}")
if __name__ == "__main__":
    extract_metadata(input("Enter folder path: "), "file_metadata.csv")
