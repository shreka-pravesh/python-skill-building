import json, datetime, os
FILE = "habits.json"
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
def mark_habit():
    habit = input("Habit name: ").lower()
    data = load_data()
    today = datetime.date.today().isoformat()
    data.setdefault(habit, []).append(today)
    save_data(data)
    print(f" Logged {habit} for today!\n")
def view_streak():
    data = load_data()
    if not data:
        print("No habits tracked yet!\n")
        return
    for habit, dates in data.items():
        print(f"{habit.title()} → {len(set(dates))} days streak")
    print()
def main():
    while True:
        print("1. Mark Habit\n2. View Streak\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            mark_habit()
        elif choice == "2":
            view_streak()
        elif choice == "3":
            break
        else:
            print("Invalid choice!\n")
if __name__ == "__main__":
    main()
