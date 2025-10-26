import os, time, random
def scan_system():
    print(" Scanning system files...")
    time.sleep(1.5)
    temp_files = random.randint(10, 50)
    print(f"Found {temp_files} temporary files.\n")
    return temp_files
def clean_system(temp_files):
    print(" Cleaning temporary files...")
    for i in range(temp_files):
        time.sleep(0.05)
    print(f" Cleaned {temp_files} files successfully!\n")
def main():
    print("=== System Cleaner Simulator ===")
    temp_files = scan_system()
    choice = input("Clean now? (y/n): ").lower()
    if choice == "y":
        clean_system(temp_files)
    else:
        print(" Cleanup canceled.")
if __name__ == "__main__":
    main()
