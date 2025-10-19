import temp_convert
print("Temperature Converter")
choice = input("C->F or F->C (enter C or F): ").upper()
val = float(input("Enter temperature: "))
if choice == "C":
    print(f"{val}°C = {temp_convert.celsius_to_fahrenheit(val):.2f}°F")
elif choice == "F":
    print(f"{val}°F = {temp_convert.fahrenheit_to_celsius(val):.2f}°C")
else:
    print("Invalid choice. Use C or F.")
