class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} engine started!")
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def display(self):
        print(f"Car: {self.brand} {self.model}")
car1 = Car("Tesla", "Model 3")
car1.display()
car1.start()
