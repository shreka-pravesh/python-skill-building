import json
from datetime import date, datetime
FILE = "health_data.json"
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
def add_meal(day, data):
    meal = input("Meal description: ")
    calories = int(input("Estimated calories: "))
    data.setdefault(day, {}).setdefault("meals", []).append({"meal": meal, "cal": calories})
    print("Meal added.")
def add_workout(day, data):
    activity = input("Workout activity: ")
    minutes = int(input("Duration (minutes): "))
    data.setdefault(day, {}).setdefault("workouts", []).append({"activity": activity, "min": minutes})
    print("Workout logged.")
def add_water(day, data):
    amount = float(input("Water (liters) added: "))
    data.setdefault(day, {}).setdefault("water", 0)
    data[day]["water"] += amount
    print("Water intake recorded.")
def daily_summary(day, data):
    d = data.get(day, {})
    meals = d.get("meals", [])
    workouts = d.get("workouts", [])
    water = d.get("water", 0)
    total_cal = sum(m["cal"] for m in meals)
    total_minutes = sum(w["min"] for w in workouts)
    print(f"\n=== Summary for {day} ===")
    print(f"Meals: {len(meals)} | Calories: {total_cal} kcal")
    print(f"Workouts: {len(workouts)} | Total minutes: {total_minutes}")
    print(f"Water: {water:.2f} L")
    print("==========================")
def main():
    data = load_data()
    today = date.today().isoformat()
    while True:
        print("\n=== Personal Health Tracker ===")
        print("1. Add meal\n2. Add workout\n3. Add water\n4. View today summary\n5. Save & Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            add_meal(today, data)
        elif ch == "2":
            add_workout(today, data)
        elif ch == "3":
            add_water(today, data)
        elif ch == "4":
            daily_summary(today, data)
        elif ch == "5":
            save_data(data)
            print("Data saved. Bye!")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
