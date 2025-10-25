import random
import string
import json
import os
VAULT = "pw_vault.json"
def generate_password(length=14):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    password += random.choices(chars, k=max(0, length - 4))
    random.shuffle(password)
    return ''.join(password)
def xor_str(s, key):
    return ''.join(chr(ord(c) ^ key) for c in s)

def load_vault(key):
    if not os.path.exists(VAULT):
        return {}
    with open(VAULT, "r") as f:
        enc = json.load(f)
    try:
        return {k: xor_str(v, key) for k, v in enc.items()}
    except Exception:
        return {}
def save_vault(data, key):
    with open(VAULT, "w") as f:
        enc = {k: xor_str(v, key) for k, v in data.items()}
        json.dump(enc, f, indent=2)
def main():
    print("=== Password Vault ===")
    try:
        key = int(input("Enter numeric vault key (1-255): "))
        if not (1 <= key <= 255): raise ValueError
    except ValueError:
        print("Invalid key.")
        return
    vault = load_vault(key)
    while True:
        print("\n1. Generate & Save Password\n2. View Vault\n3. Delete Entry\n4. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            name = input("Account name (e.g., Gmail): ").strip()
            length = int(input("Password length (12 recommended): ") or 14)
            pw = generate_password(length)
            vault[name] = pw
            save_vault(vault, key)
            print(f" Saved for '{name}': {pw}")
        elif ch == "2":
            if not vault:
                print("Vault is empty.")
            else:
                for k, v in vault.items():
                    print(f"{k} -> {v}")
        elif ch == "3":
            name = input("Entry name to delete: ").strip()
            if name in vault:
                vault.pop(name)
                save_vault(vault, key)
                print("Deleted.")
            else:
                print("Entry not found.")
        elif ch == "4":
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
