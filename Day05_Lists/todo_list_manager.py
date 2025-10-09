# A simple to-do list manager using Python lists

tasks = []
def show_tasks():
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task(task):
    tasks.append(task)
    print(f" '{task}' added to your list.")
def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f" '{removed}' removed from your list.")
    except IndexError:
        print("Invalid task number!")
while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        new_task = input("Enter new task: ")
        add_task(new_task)
    elif choice == "3":
        show_tasks()
        try:
            num = int(input("Enter task number to remove: "))
            remove_task(num)
        except ValueError:
            print("Please enter a valid number!")
    elif choice == "4":
        print(" Exiting... Have a productive day!")
        break
    else:
        print(" Invalid choice. Try again!")
