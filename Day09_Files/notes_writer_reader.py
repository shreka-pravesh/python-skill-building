# Program: Notes Writer and Reader
# Concept: Writing and reading text files in Python

def write_notes():
    with open("notes.txt", "a") as f:
        note = input("Enter a note: ")
        f.write(note + "\n")
        print(" Note added successfully!")
def read_notes():
    try:
        with open("notes.txt", "r") as f:
            print("\n Your Notes:")
            print(f.read())
    except FileNotFoundError:
        print(" No notes found. Start writing one!")
while True:
    print("\n1. Write Note\n2. Read Notes\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        write_notes()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        print(" Exiting Notes App.")
        break
    else:
        print("Invalid choice! Try again.")
