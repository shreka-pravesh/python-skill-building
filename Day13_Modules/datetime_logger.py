from datetime import datetime
def log_action(action, file="activity.txt"):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "a") as f:
        f.write(f"[{time}] {action}\n")
        
if __name__ == "__main__":
    name = input("Enter your name: ")
    log_action(f"{name} opened the program")
    if input("Log an action now? (y/n): ").lower() == "y":
        log_action(input("Describe action: "))
    print("Done. Check activity.txt for logs.")
