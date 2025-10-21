import time
from datetime import datetime
def set_reminder():
    reminder_time = input("Enter reminder time (HH:MM:SS): ")
    message = input("Enter reminder message: ")
    print(f"Reminder set for {reminder_time} ")
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == reminder_time:
            print(f"\n Reminder: {message}\n")
            break
        time.sleep(1)
def main():
    while True:
        print("\n=== Reminder Notifier ===")
        print("1. Set Reminder\n2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            set_reminder()
        elif choice == "2":
            print("Goodbye! ")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
