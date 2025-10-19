from datetime import datetime, timedelta
def date_planner():
    print("=== Date Planner ===")
    today = datetime.now()
    print("Today:", today.strftime("%Y-%m-%d"))
    while True:
        print("\n1. Add days\n2. Subtract days\n3. Days between two dates\n4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            days = int(input("Enter days to add: "))
            print("Future Date:", (today + timedelta(days=days)).strftime("%Y-%m-%d"))
        elif choice == '2':
            days = int(input("Enter days to subtract: "))
            print("Past Date:", (today - timedelta(days=days)).strftime("%Y-%m-%d"))
        elif choice == '3':
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            diff = abs((datetime.fromisoformat(d2) - datetime.fromisoformat(d1)).days)
            print(f"Difference: {diff} days")
        elif choice == '4':
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    date_planner()
