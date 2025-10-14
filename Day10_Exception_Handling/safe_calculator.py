# Calculator with error handling for invalid inputs

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Operator (+,-,*,/): ")
    if op == "+": print("Result:", a + b)
    elif op == "-": print("Result:", a - b)
    elif op == "*": print("Result:", a * b)
    elif op == "/": print("Result:", a / b)
    else: print("Invalid operator!")
except ValueError:
    print(" Enter valid numbers only!")
except ZeroDivisionError:
    print(" Division by zero is not allowed!")
