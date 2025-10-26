import csv
from statistics import mean
def read_csv(file):
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data
def analyze_sales(data):
    sales = [float(d["sales"]) for d in data]
    avg_sales = mean(sales)
    max_sale = max(sales)
    min_sale = min(sales)
    print(f" Average Sales: {avg_sales:.2f}")
    print(f" Highest Sale: {max_sale}")
    print(f" Lowest Sale: {min_sale}")
def main():
    filename = input("Enter CSV filename (ex: sales_data.csv): ")
    try:
        data = read_csv(filename)
        analyze_sales(data)
    except FileNotFoundError:
        print(" File not found. Make sure the CSV file exists.")
if __name__ == "__main__":
    main()
