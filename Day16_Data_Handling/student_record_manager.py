import json
import os
FILE = "students.json"
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
def add_student():
    data = load_data()
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    grade = input("Enter grade: ")
    data.append({"name": name, "roll": roll, "grade": grade})
    save_data(data)
    print(" Student added!")
def view_students():
    data = load_data()
    print("\n=== Student Records ===")
    for s in data:
        print(f"{s['roll']} - {s['name']} ({s['grade']})")
def search_student():
    data = load_data()
    roll = input("Enter roll number to search: ")
    for s in data:
        if s["roll"] == roll:
            print(f"Found: {s['name']} - Grade {s['grade']}")
            return
    print("No student found!")
def main():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": search_student()
        elif choice == "4": break
        else: print("Invalid choice!")
if __name__ == "__main__":
    main()
