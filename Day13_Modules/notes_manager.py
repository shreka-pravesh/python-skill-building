import file_utils
F = "notes_db.txt"
def add_note():
    note = input("Enter note: ")
    file_utils.append_note(F, note)
    print(" Note saved.")
def view_notes():
    data = file_utils.read_notes(F)
    print("\n=== Your Notes ===")
    print(data or "No notes yet.")
def menu():
    while True:
        print("\n1. Add Note\n2. View Notes\n3. Exit")
        c = input("Choice: ")
        if c == "1":
            add_note()
        elif c == "2":
            view_notes()
        elif c == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    menu()
