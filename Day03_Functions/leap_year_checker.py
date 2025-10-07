# Leap Year Checker using Function

def is_leap_year(year):
    # A leap year is divisible by 4, but not by 100 unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
