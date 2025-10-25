import json
import time
from datetime import datetime
FILE = "reminders.json"
def load_reminders():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_reminders(rem):
    with open(FILE, "w") as f:
        json.dump(rem, f, indent=2)
def add_reminder():
    msg = input("Reminder message: ").strip()
    at = input("Enter reminder time (YYYY-MM-DD HH:MM): ").strip()
    try:
        datetime.fromisoformat(at)
    except ValueError:
        print("Invalid datetime format.")
        return
    rem = load_reminders()
    rem.append({"time": at, "message": msg, "done": False})
    save_reminders(rem)
    print(" Reminder saved.")
def check_reminders():
    rem = load_reminders()
    now = datetime.now()
    changed = False
    for r in rem:
        if not r.get("done") and datetime.fromisoformat(r["time"]) <= now:
            print(f"\n Reminder: {r['message']} (scheduled: {r['time']})")
            r["done"] = True
            changed = True
    if changed:
        save_reminders(rem)
def main():
    print("=== Smart Task Reminder ===")
    while True:
        print("\n1. Add reminder\n2. Check reminders now\n3. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            add_reminder()
        elif ch == "2":
            print("Checking reminders...")
            check_reminders()
        elif ch == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
