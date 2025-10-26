import json, datetime, os
FILENAME = "projects.json"
def load_projects():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []
def save_projects(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)
def add_project():
    name = input("Project Name: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    tasks = input("Task list (comma separated): ").split(",")
    project = {"name": name, "deadline": deadline, "tasks": [t.strip() for t in tasks], "status": "Active"}
    data = load_projects()
    data.append(project)
    save_projects(data)
    print(" Project added successfully!\n")
def show_projects():
    data = load_projects()
    if not data:
        print("No projects found.\n")
        return
    print("\n--- Project List ---")
    for p in data:
        print(f"{p['name']} | Deadline: {p['deadline']} | Status: {p['status']}")
    print()
def update_status():
    name = input("Enter project name: ")
    data = load_projects()
    for p in data:
        if p["name"].lower() == name.lower():
            p["status"] = input("New status (Active/Completed/Hold): ")
            save_projects(data)
            print("Status updated!\n")
            return
    print("Project not found.\n")
def main():
    while True:
        print("1. Add Project\n2. Show Projects\n3. Update Status\n4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_project()
        elif choice == "2":
            show_projects()
        elif choice == "3":
            update_status()
        elif choice == "4":
            break
        else:
            print("Invalid option!\n")
if __name__ == "__main__":
    main()
