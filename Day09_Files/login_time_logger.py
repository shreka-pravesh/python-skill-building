# Record user login time with timestamp

from datetime import datetime
file = "login_log.txt"
name = input("Enter username: ")
with open(file, "a") as f:
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{name} logged in at {time}\n")
print(f" Login time saved for {name}!")
if input("View log history? (y/n): ").lower() == "y":
    print(open(file).read())
