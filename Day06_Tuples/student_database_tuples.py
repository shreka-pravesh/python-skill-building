# Program to manage a simple student database using tuples

students = (
    ("101", "Leena", 18, "AIML"),
    ("102", "Jeelani", 19, "IT"),
    ("103", "Shreka", 20, "CSE"),
    ("104", "Tarak", 18, "AIDS"),
)
print("=== Student Database ===")
print(f"{'ID':<5} {'Name':<10} {'Age':<5} {'Department'}")
print("-" * 30)
for sid, name, age, dept in students:
    print(f"{sid:<5} {name:<10} {age:<5} {dept}")
print("\nTotal Students:", len(students))
