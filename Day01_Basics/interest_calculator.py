# This program helps you find simple interest easily

print("Simple Interest Calculator")

amount = float(input("Enter the principal amount: "))
time = float(input("Enter time in years: "))
rate = float(input("Enter rate of interest: "))

interest = (amount * time * rate) / 100

print("Simple Interest is:", interest)
print("Thank you for using this mini calculator.")
