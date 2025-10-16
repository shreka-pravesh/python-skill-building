class Device:
    def turn_on(self):
        print("Device is now ON")
class SmartPhone(Device):
    def turn_on(self):
        super().turn_on()
        print("Smartphone booted with Face ID and apps loaded")
phone = SmartPhone()
phone.turn_on()
