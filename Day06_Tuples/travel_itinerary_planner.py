# ✈️ Travel Itinerary Planner using Tuples
# This program helps travelers organize their trip details and display a complete schedule.
# Each tuple holds: (Destination, Travel Mode, Distance_km, Days)

itinerary = (
    ("Chennai", "Train", 350, 2),
    ("Bangalore", "Bus", 280, 3),
    ("Goa", "Flight", 870, 5),
    ("Mumbai", "Flight", 1030, 4),
    ("Delhi", "Flight", 1760, 6)
)
def display_itinerary(trip_data):
    print("\n=== 🧳 Travel Itinerary Summary ===")
    print(f"{'Place':<12}{'Mode':<10}{'Distance(km)':<15}{'Days'}")
    print("-" * 45)
    for city, mode, distance, days in trip_data:
        print(f"{city:<12}{mode:<10}{distance:<15}{days}")
    print("-" * 45)
def total_distance(trip_data):
    total_km = sum(city[2] for city in trip_data)
    print(f"  Total Distance to be Covered: {total_km} km")
def total_days(trip_data):
    total = sum(city[3] for city in trip_data)
    print(f" Total Travel Days: {total}")
def longest_trip(trip_data):
    longest = max(trip_data, key=lambda x: x[2])
    print(f" Longest Trip: {longest[0]} ({longest[2]} km by {longest[1]})")
def travel_summary(trip_data):
    print("\n Quick Summary:")
    total_distance(trip_data)
    total_days(trip_data)
    longest_trip(trip_data)
print("Welcome to Travel Itinerary Planner")
display_itinerary(itinerary)
travel_summary(itinerary)
print("\n Itinerary ready! Have a safe and wonderful journey.")
