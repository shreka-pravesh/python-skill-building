# Program: Simple Log Generator
# Concept: Create a text log with timestamps for actions

import datetime
def log_event(event):
    with open("activity_log.txt", "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] {event}\n")
while True:
    print("\n1. Add Log\n2. View Logs\n3. Exit")
    ch = input("Enter your choice: ")
    if ch == "1":
        event = input("Describe the event: ")
        log_event(event)
        print(" Event logged successfully.")
    elif ch == "2":
        try:
            with open("activity_log.txt", "r") as f:
                print("\n Activity Log:\n" + f.read())
        except FileNotFoundError:
            print("No logs found.")
    elif ch == "3":
        print(" Exiting Log Generator.")
        break
    else:
        print("Invalid option.")
