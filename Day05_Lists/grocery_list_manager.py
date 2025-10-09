# Simple Grocery List Manager

def show_items(groceries):
    if not groceries:
        print("\n Your grocery list is empty!")
    else:
        print("\n Your Grocery List:")
        for i, item in enumerate(groceries, 1):
            print(f"{i}. {item}")
def add_item(groceries):
    item = input("Enter item to add: ").capitalize()
    groceries.append(item)
    print(f" '{item}' added successfully.")
def remove_item(groceries):
    show_items(groceries)
    try:
        num = int(input("Enter item number to remove: "))
        removed = groceries.pop(num - 1)
        print(f" '{removed}' removed successfully.")
    except (ValueError, IndexError):
        print("Invalid choice. Try again!")
groceries = []
while True:
    print("\n=== Grocery List Menu ===")
    print("1. Show Items")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        show_items(groceries)
    elif choice == '2':
        add_item(groceries)
    elif choice == '3':
        remove_item(groceries)
    elif choice == '4':
        print(" Exiting... Happy Shopping!")
        break
    else:
        print("Invalid option, please try again.")
