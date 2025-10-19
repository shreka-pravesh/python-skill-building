import math
def math_toolbox():
    print("=== Math Toolbox ===")
    print("1. Square Root\n2. Power\n3. Factorial\n4. Trigonometric (sin, cos, tan)\n5. Exit")
    while True:
        choice = input("\nEnter choice (1-5): ")
        if choice == '1':
            n = float(input("Enter number: "))
            print("Square Root:", math.sqrt(n))
        elif choice == '2':
            a, b = map(float, input("Enter base and exponent: ").split())
            print("Result:", math.pow(a, b))
        elif choice == '3':
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))
        elif choice == '4':
            angle = float(input("Enter angle in degrees: "))
            print(f"sin({angle}) = {round(math.sin(math.radians(angle)),2)}")
            print(f"cos({angle}) = {round(math.cos(math.radians(angle)),2)}")
            print(f"tan({angle}) = {round(math.tan(math.radians(angle)),2)}")
        elif choice == '5':
            print("Exiting Math Toolbox...")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    math_toolbox()
