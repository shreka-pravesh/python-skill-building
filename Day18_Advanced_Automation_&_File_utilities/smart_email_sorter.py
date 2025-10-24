import json
import os
CATEGORIES = {
    "Work": ["project", "meeting", "deadline", "client"],
    "Personal": ["family", "birthday", "trip", "friend"],
    "Promotions": ["offer", "discount", "sale", "deal"]
}
def categorize(subject):
    for cat, words in CATEGORIES.items():
        if any(word in subject.lower() for word in words):
            return cat
    return "Others"
def main():
    if not os.path.exists("emails.txt"):
        print(" No 'emails.txt' file found!")
        return
    with open("emails.txt") as f:
        subjects = [line.strip() for line in f if line.strip()]
    sorted_data = {}
    for sub in subjects:
        cat = categorize(sub)
        sorted_data.setdefault(cat, []).append(sub)
    with open("sorted_emails.json", "w") as f:
        json.dump(sorted_data, f, indent=4)
    print("\n Emails categorized and saved to sorted_emails.json\n")
    for cat, subs in sorted_data.items():
        print(f"{cat} ({len(subs)}):")
        for s in subs:
            print(f"  - {s}")
if __name__ == "__main__":
    main()
