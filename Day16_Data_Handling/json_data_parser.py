import json
def read_json():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            print("\n=== JSON Data ===")
            for key, value in data.items():
                print(f"{key}: {value}")
    except FileNotFoundError:
        print("data.json not found!")
    except json.JSONDecodeError:
        print("Invalid JSON format!")
if __name__ == "__main__":
    read_json()
