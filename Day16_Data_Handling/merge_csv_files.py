import csv
import glob
def merge_csv(output_file="merged.csv"):
    csv_files = glob.glob("data_*.csv")
    with open(output_file, "w", newline="") as out:
        writer = csv.writer(out)
        for file in csv_files:
            with open(file, "r") as f:
                reader = csv.reader(f)
                writer.writerows(reader)
    print(" CSV files merged into", output_file)
if __name__ == "__main__":
    merge_csv()
