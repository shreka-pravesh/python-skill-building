# Program to calculate average, median, and range of numbers stored in a tuple

numbers = (12, 45, 67, 89, 34, 22, 90, 55, 76, 43)
sorted_numbers = sorted(numbers)
average = sum(numbers) / len(numbers)
median = sorted_numbers[len(sorted_numbers)//2]
value_range = max(numbers) - min(numbers)
print("Numbers:", numbers)
print("Sorted:", sorted_numbers)
print(f"Average: {average:.2f}")
print(f"Median: {median}")
print(f"Range: {value_range}")
