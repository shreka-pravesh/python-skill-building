# Program to combine tuples and filter values greater than a limit

tuple_a = (10, 25, 36, 45, 50)
tuple_b = (22, 18, 75, 60, 15)
combined = tuple_a + tuple_b
filtered = tuple(num for num in combined if num > 30)
print("Tuple A:", tuple_a)
print("Tuple B:", tuple_b)
print("Combined Tuple:", combined)
print("Filtered (values > 30):", filtered)
print("Total Filtered Items:", len(filtered))
