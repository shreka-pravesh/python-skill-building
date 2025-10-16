class Course:
    def __init__(self, title):
        self.title = title
    def show_info(self):
        print(f"Course: {self.title}")
class FreeCourse(Course):
    def price(self):
        print("This course is free!")
class PaidCourse(Course):
    def price(self):
        print("This course costs ₹499.")
free = FreeCourse("Python Basics")
paid = PaidCourse("Advanced OOP")
free.show_info()
free.price()
paid.price()
