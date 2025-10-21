import time
def task_timer():
    print("=== Task Timer ===")
    task = input("Enter task name: ")
    input("Press ENTER to start...")
    start = time.time()
    print("Timer started. Press ENTER to stop.")
    input()
    end = time.time()
    duration = round((end - start)/60, 2)
    print(f"Task '{task}' took {duration} minutes.")
    with open("task_log.txt", "a") as f:
        f.write(f"{task} - {duration} minutes\n")
if __name__ == "__main__":
    task_timer()
