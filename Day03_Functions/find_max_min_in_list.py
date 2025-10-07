# Find Maximum and Minimum in a List using Functions

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
data = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum number is:", find_max(data))
print("Minimum number is:", find_min(data))
