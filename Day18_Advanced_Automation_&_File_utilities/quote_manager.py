import json
import random
import os
FILE = "quotes.json"
def load_quotes():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)
def save_quotes(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
def show_random_quote():
    quotes = load_quotes()
    if not quotes:
        print("No quotes yet! Add one first.")
        return
    print(f"\n Quote of the Day:\n{random.choice(quotes)}")
def add_quote():
    quote = input("Enter new quote: ")
    data = load_quotes()
    data.append(quote)
    save_quotes(data)
    print(" Quote added!")
def delete_quote():
    data = load_quotes()
    if not data:
        print("No quotes to delete.")
        return
    for i, q in enumerate(data, 1):
        print(f"{i}. {q}")
    idx = int(input("Select quote number to delete: ")) - 1
    if 0 <= idx < len(data):
        removed = data.pop(idx)
        save_quotes(data)
        print(f" Deleted: {removed}")
    else:
        print("Invalid choice.")
def main():
    while True:
        print("\n=== Quote Manager ===")
        print("1. Show random quote\n2. Add quote\n3. Delete quote\n4. Exit")
        ch = input("Enter choice: ")
        if ch == "1": show_random_quote()
        elif ch == "2": add_quote()
        elif ch == "3": delete_quote()
        elif ch == "4": break
        else: print(" Invalid choice.")
if __name__ == "__main__":
    main()
