import stats_utils
data = list(map(float, input("Enter numbers separated by space: ").split()))
if not data:
    print("No numbers provided.")
else:
    print(f"Mean: {stats_utils.mean(data):.2f}")
    print(f"Median: {stats_utils.median(data):.2f}")
