# Write and read diary entries

def write_entry():
    with open("diary.txt", "a") as f:
        f.write(input("Entry: ") + "\n")
def read_entries():
    try: print(open("diary.txt").read())
    except FileNotFoundError:
        print("No entries yet.")
write_entry() if input("W for write, R for read: ").lower() == "w" else read_entries()
