# Program to check stock availability using sets

store_items = {"milk", "bread", "butter", "eggs", "jam", "chips"}
requested_items = {"butter", "jam", "coffee", "eggs", "biscuits"}
available = requested_items.intersection(store_items)
not_available = requested_items.difference(store_items)
print(" Items available in stock:", available)
print(" Items not available:", not_available)
if not_available:
    print("\n Restock the following items soon:")
    for item in not_available:
        print("-", item)
