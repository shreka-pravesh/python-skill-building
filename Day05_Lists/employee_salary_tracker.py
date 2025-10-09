# Simple Employee Salary Tracker

employees = []
def add_employee():
    name = input("Enter employee name: ").capitalize()
    salary = float(input("Enter salary: "))
    employees.append([name, salary])
    print(f" {name}'s data added successfully!")
def show_employees():
    if not employees:
        print("\nNo employee data found.")
    else:
        print("\n👩‍💼 Employee Salary List:")
        for i, (name, salary) in enumerate(employees, 1):
            print(f"{i}. {name} - ₹{salary:.2f}")
def show_summary():
    if employees:
        salaries = [emp[1] for emp in employees]
        print("\n Salary Summary:")
        print(f"Total Employees: {len(salaries)}")
        print(f"Average Salary: ₹{sum(salaries)/len(salaries):.2f}")
        print(f"Highest Salary: ₹{max(salaries):.2f}")
        print(f"Lowest Salary: ₹{min(salaries):.2f}")
    else:
        print("\nNo data to summarize!")
while True:
    print("\n=== Employee Salary Tracker ===")
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Show Salary Summary")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_employee()
    elif choice == '2':
     show_employees()
    elif choice == '3':
        show_summary()
    elif choice == '4':
        print(" Exiting... Have a great day!")
        break
    else:
        print(" Invalid choice, try again!")
