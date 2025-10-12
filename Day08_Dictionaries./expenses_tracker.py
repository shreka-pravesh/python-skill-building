# Program: Simple Expense Tracker
# Concept: Dictionary with sum and update

expenses = {}
while True:
    cat = input("Enter category (Food/Travel/Exit): ").title()
    if cat == "Exit":
        break
    amount = float(input("Enter amount: ₹"))
    expenses[cat] = expenses.get(cat, 0) + amount
print("\n Expense Summary:")
for c, a in expenses.items():
    print(f"{c}: ₹{a}")
print(f"Total: ₹{sum(expenses.values())}")
