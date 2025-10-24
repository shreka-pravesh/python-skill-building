import random
import json
from datetime import datetime, timedelta
def generate_weather(city):
    """Generate random weather data for a given city."""
    conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Stormy", "Drizzle"]
    today = datetime.now()
    forecast = []
    for i in range(3):
        date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        temp = random.randint(20, 38)
        humidity = random.randint(40, 90)
        condition = random.choice(conditions)
        forecast.append({
            "date": date,
            "temperature": f"{temp}°C",
            "humidity": f"{humidity}%",
            "condition": condition
        })
    return {
        "city": city.title(),
        "generated_at": today.strftime("%Y-%m-%d %H:%M:%S"),
        "forecast": forecast
    }
def display_weather(data):
    """Display weather data neatly."""
    print(f"\n Weather Forecast for {data['city']}")
    print(f"Generated on: {data['generated_at']}")
    print("-" * 40)
    for day in data["forecast"]:
        print(f"{day['date']} → {day['condition']} | {day['temperature']} | Humidity: {day['humidity']}")
    print("-" * 40)
def save_to_file(data):
    """Save weather data to a JSON file."""
    filename = f"{data['city'].lower()}_forecast.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f" Saved to {filename}")
def main():
    print("=== Mini Weather Fetcher ===")
    city = input("Enter city name: ").strip()
    if not city:
        print(" Please enter a valid city name.")
        return
    data = generate_weather(city)
    display_weather(data)
    save = input("Do you want to save this report? (y/n): ").lower()
    if save == "y":
        save_to_file(data)
        print(" Weather report saved successfully!")
    else:
        print(" Data not saved. Have a nice day!")
if __name__ == "__main__":
    main()
