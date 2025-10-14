# Safely open and read a file with error handling

try:
    name = input("Enter file name: ")
    with open(name, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(" File not found!")
except PermissionError:
    print(" Permission denied!")
except Exception as e:
    print("Unknown error:", e)
