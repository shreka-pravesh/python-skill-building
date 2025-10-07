# Student Grade Calculator using Functions

def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)
def find_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"
marks = list(map(float, input("Enter your marks separated by space: ").split()))
average = calculate_average(marks)
grade = find_grade(average)
print(f"Your Average: {average:.2f}")
print(f"Your Grade: {grade}")
