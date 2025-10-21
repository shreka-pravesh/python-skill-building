def add_note():
    with open("notes.txt", "a") as f:
        note = input("Write your note: ")
        f.write(note + "\n")
    print("Note added successfully!")
def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        print("\n=== Your Notes ===")
        for n in notes:
            print("-", n.strip())
    except FileNotFoundError:
        print("No notes found!")
def search_note():
    keyword = input("Enter keyword to search: ").lower()
    found = False
    try:
        with open("notes.txt", "r") as f:
            for line in f:
                if keyword in line.lower():
                    print("Found:", line.strip())
                    found = True
        if not found:
            print("No matching notes found.")
    except FileNotFoundError:
        print("Notes file missing!")
def main():
    while True:
        print("\n=== Personal Notebook ===")
        print("1. Add Note\n2. View Notes\n3. Search Notes\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1': add_note()
        elif choice == '2': view_notes()
        elif choice == '3': search_note()
        elif choice == '4': break
        else: print("Invalid option!")
if __name__ == "__main__":
    main()
