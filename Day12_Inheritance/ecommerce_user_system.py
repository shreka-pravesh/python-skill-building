class User:
    def __init__(self, username):
        self.username = username
    def login(self):
        print(f"{self.username} logged in successfully.")
class Buyer(User):
    def purchase(self, item):
        print(f"{self.username} purchased {item}.")
class Seller(User):
    def add_item(self, item):
        print(f"{self.username} added {item} to the store.")
buyer1 = Buyer("Shreka")
seller1 = Seller("Jeelani")
buyer1.login()
buyer1.purchase("Sneakers")
seller1.login()
seller1.add_item("Wrist Watch")
