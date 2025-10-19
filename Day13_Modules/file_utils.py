from datetime import datetime
def append_note(filename, note):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{time}] {note}\n")

def read_notes(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
