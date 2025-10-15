class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. Current Balance: ₹{self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}. Balance: ₹{self.balance}")
        else:
            print("Insufficient funds!")
account1 = BankAccount("Shreka", 155000)
account1.deposit(5500)
account1.withdraw(3000)
