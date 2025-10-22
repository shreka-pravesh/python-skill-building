import csv
def add_user():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    with open("users.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, age, email])
    print(" User added successfully!")
def view_users():
    try:
        with open("users.csv", "r") as f:
            reader = csv.reader(f)
            print("\n=== User List ===")
            for row in reader:
                print(f"Name: {row[0]}, Age: {row[1]}, Email: {row[2]}")
    except FileNotFoundError:
        print("No user data found!")
def main():
    while True:
        print("\n1. Add User\n2. View Users\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1": add_user()
        elif choice == "2": view_users()
        elif choice == "3": break
        else: print("Invalid choice!")
if __name__ == "__main__":
    main()
