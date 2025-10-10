# Program to store employee details and calculate salary stats using tuples

employees = (
    ("E101", "jeelani", 150000, "HR" ),
    ("E102", "Shreka", 150000, "Developer" ),
    ("E103", "Leena", 100000, "IT" ),
    ("E104", "Nivetha", 125000, "Marketing" ),
    ("E105", "Tarak", 100000, "IT" ),
)
print("=== Employee Payroll Summary ===\n")
print(f"{'ID':<6} {'Name':<10} {'Dept':<12} {'Salary'}")
print("-" * 40)
for emp_id, name, dept, salary in employees:
    print(f"{emp_id:<6} {name:<10} {dept:<12} ₹{salary}")
salaries = tuple(emp[2] for emp in employees)
total = sum(salaries)
average = total / len(salaries)
highest = max(salaries)
lowest = min(salaries)
print("\nTotal Salary Expense: ₹", total)
print("Average Salary: ₹", round(average, 2))
print("Highest Salary: ₹", highest)
print("Lowest Salary: ₹", lowest)
