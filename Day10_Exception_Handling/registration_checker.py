# Validate simple registration details

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format!")
    print(f" {name} registered successfully!")
except ValueError as e:
    print(" Error:", e)
except Exception as e:
    print("Unexpected error:", e)
