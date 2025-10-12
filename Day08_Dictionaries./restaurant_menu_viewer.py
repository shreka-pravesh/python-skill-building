# Program: Restaurant Menu Viewer
# Concept: Dictionary display with input checking

menu = {"Pizza": 250, "Burger": 150, "Fries": 100, "Juice": 80}
print("🍽️ Food Menu 🍽️ ")
for item, price in menu.items():
    print(f"- {item}: ₹{price}")
order = input("\nWhat would you like to order? ").title()
if order in menu:
    print(f" {order} costs ₹{menu[order]}")
else:
    print(" Item not available.")
