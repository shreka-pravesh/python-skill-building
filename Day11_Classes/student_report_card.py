class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
student1 = Student("Jeelani", [95, 92, 93, 90])
student1.display()
