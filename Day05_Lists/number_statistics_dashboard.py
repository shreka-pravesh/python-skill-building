# Program to show various statistics of a number list

def number_stats(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    squared = [n**2 for n in numbers]
    print("\n Number Statistics:")
    print(f"Numbers Entered: {numbers}")
    print(f"Even Numbers: {even}")
    print(f"Odd Numbers: {odd}")
    print(f"Squared Values: {squared}")
    print(f"Sum: {sum(numbers)} | Average: {sum(numbers)/len(numbers):.2f}")
print("=== Number Statistics Dashboard ===")
nums = list(map(int, input("Enter numbers separated by space: ").split()))
number_stats(nums)
