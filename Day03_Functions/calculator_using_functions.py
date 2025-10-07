# Simple Calculator using Functions 

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b 
def multiply(a, b):
    return a * b
def divide(A, b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b
print("Select an operation: + - * /")
operator = input("Enter your choice: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if operator == '+':
    print("result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
else:
    printf("Invalid operator! Please try again.")

