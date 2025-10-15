class ShoppingCart:
    def __init__(self):
        self.cart = {}
    def add_item(self, name, price):
        self.cart[name] = price
        print(f"Added {name} for ₹{price}")
    def show_cart(self):
        total = sum(self.cart.values())
        print("\nYour Cart:")
        for item, price in self.cart.items():
            print(f"{item} - ₹{price}")
        print(f"Total: ₹{total}")
cart = ShoppingCart()
cart.add_item("T-Shirt", 799)
cart.add_item("Shoes", 1999)
cart.show_cart()
