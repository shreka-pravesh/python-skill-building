def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    nums = sorted(numbers)
    n = len(nums)
    mid = n // 2
    return (nums[mid] if n % 2 else (nums[mid-1] + nums[mid]) / 2)
