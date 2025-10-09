# Find the topper from a list of students and their scores

students = []
print("=== Class Topper Finder ===")
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name of student {i+1}: ").capitalize()
    score = float(input(f"Enter {name}'s score: "))
    students.append([name, score])
students.sort(key=lambda x: x[1], reverse=True)
print("\n Class Rank List:")
for i, (name, score) in enumerate(students, 1):
    print(f"{i}. {name} - {score}")
print(f"\n Topper: {students[0][0]} with {students[0][1]} marks!")
