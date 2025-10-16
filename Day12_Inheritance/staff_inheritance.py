class Staff:
    def __init__(self, name):
        self.name = name
class Teacher(Staff):
    def role(self):
        return "Teaching students"
class Administrator(Staff):
    def manage(self):
        return "Managing school records"
class HeadMaster(Teacher, Administrator):
    def duties(self):
        print(f"{self.name} is responsible for {self.role()} and {self.manage()}")
head = HeadMaster("Mr. Arjun")
head.duties()
