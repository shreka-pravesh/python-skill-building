# Program to manage and analyze student marks

def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    print("\n Student Marks Summary:")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
print("=== Student Marks Analyzer ===")
marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    score = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(score)
print("\nMarks Entered:", marks)
analyze_marks(marks)
