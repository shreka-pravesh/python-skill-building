# Handle division errors and retry option

while True:
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print("Result:", a / b)
        break
    except ValueError:
        print(" Please enter valid numbers!")
    except ZeroDivisionError:
        print(" Denominator cannot be zero!")
