def clean_log(file_name):
    if not file_name.endswith(".log"):
        print(" Only .log files are allowed.")
        return
    with open(file_name, "r") as f:
        lines = f.readlines()
    cleaned = [line.strip().replace("#", "") for line in lines if line.strip()]
    with open(file_name, "w") as f:
        f.write("\n".join(cleaned))
    print(f" Cleaned {len(cleaned)} log lines saved in {file_name}")
if __name__ == "__main__":
    clean_log(input("Enter log file name: "))
