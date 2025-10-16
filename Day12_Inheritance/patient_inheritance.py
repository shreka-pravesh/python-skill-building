class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        print(f"Patient Name: {self.name}, Age: {self.age}")
class InPatient(Patient):
    def __init__(self, name, age, room_no):
        super().__init__(name, age)
        self.room_no = room_no
    def admit(self):
        print(f"{self.name} admitted to Room {self.room_no}")
class SurgeryPatient(InPatient):
    def __init__(self, name, age, room_no, surgery_type):
        super().__init__(name, age, room_no)
        self.surgery_type = surgery_type
    def schedule_surgery(self):
        print(f"Surgery scheduled for {self.name} - Type: {self.surgery_type}")
patient1 = SurgeryPatient("Ananya", 26, 101, "Appendix Removal")
patient1.details()
patient1.admit()
patient1.schedule_surgery()
