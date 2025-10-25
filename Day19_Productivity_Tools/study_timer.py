import time
from datetime import datetime
LOGFILE = "study_sessions.log"
def countdown(seconds, label="Timer"):
    try:
        while seconds:
            m, s = divmod(seconds, 60)
            print(f"\r{label} - {m:02d}:{s:02d}", end="", flush=True)
            time.sleep(1)
            seconds -= 1
        print("\r" + " " * 40, end="\r")
    except KeyboardInterrupt:
        print("\nInterrupted.")
        return False
    return True
def log_session(task, work_minutes):
    with open(LOGFILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} | {task} | {work_minutes} min\n")
def main():
    print("=== Study Timer (Pomodoro) ===")
    task = input("Task name: ").strip() or "Study"
    try:
        work = int(input("Work minutes (default 25): ") or 25)
        short_break = int(input("Short break minutes (default 5): ") or 5)
        cycles = int(input("Number of cycles (default 4): ") or 4)
    except ValueError:
        print("Invalid numbers; using defaults.")
        work, short_break, cycles = 25, 5, 4
    for c in range(1, cycles + 1):
        print(f"\nSession {c}/{cycles}: Work for {work} minutes.")
        if not countdown(work * 60, label="Work"):
            break
        log_session(task, work)
        if c < cycles:
            print(f"Short break for {short_break} minutes.")
            if not countdown(short_break * 60, label="Break"):
                break
    print("All cycles completed. Good job!")
if __name__ == "__main__":
    main()
