import calendar, json
from datetime import datetime
def load_events(file="events.json"):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_events(events, file="events.json"):
    with open(file, 'w') as f:
        json.dump(events, f, indent=2)
def show_calendar(events):
    now = datetime.now()
    year, month = now.year, now.month
    cal = calendar.monthcalendar(year, month)
    print(f"\n {calendar.month_name[month]} {year}")
    print("Mon Tue Wed Thur Fri Sat Sun")
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            elif str(day) in events:
                print(f"*{str(day).rjust(2)}", end=" ")
            else:
                print(f" {str(day).rjust(2)}", end=" ")
        print()
    print("\n* = Event Day\n")
def main():
    events = load_events()
    while True:
        print("=== Event Calendar ===")
        print("1. View Calendar\n2. Add Event\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            show_calendar(events)
        elif choice == '2':
            day = input("Enter day number: ")
            note = input("Enter event note: ")
            events[day] = note
            save_events(events)
            print("Event saved!")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
