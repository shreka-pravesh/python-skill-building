# Program: Personal To-Do Task Manager
# Concept: Dictionary with nested data and status updates

print(" Personal Task Manager")
tasks = {}
while True:
    print("\n1. Add Task\n2. Mark Complete\n3. View Tasks\n4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        title = input("Task title: ").title()
        desc = input("Task description: ")
        tasks[title] = {"description": desc, "status": "Pending"}
        print(f" Task '{title}' added.")
    elif choice == "2":
        title = input("Enter task title to mark complete: ").title()
        if title in tasks:
            tasks[title]["status"] = "Done"
            print(f" Task '{title}' marked as complete.")
        else:
            print(" Task not found.")
    elif choice == "3":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\n All Tasks:")
            for name, info in tasks.items():
                print(f"- {name}: {info['description']} [{info['status']}]")
    elif choice == "4":
        print(" Exiting Task Manager. Stay productive!")
        break
    else:
        print("Invalid choice, try again.")
