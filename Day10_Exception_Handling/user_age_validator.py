# Get valid user age and check eligibility

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("You are eligible to proceed." if age >= 18 else "You are underaged.")
except ValueError as e:
    print(" Invalid input:", e)
