import os
def xor_bytes(data: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in data)
def write_encrypted(note_text, filename, key):
    data = note_text.encode("utf-8")
    enc = xor_bytes(data, key)
    with open(filename, "wb") as f:
        f.write(enc)
def read_encrypted(filename, key):
    with open(filename, "rb") as f:
        data = f.read()
    dec = xor_bytes(data, key)
    try:
        return dec.decode("utf-8")
    except UnicodeDecodeError:
        return None
def list_encrypted_notes():
    return [f for f in os.listdir(".") if f.endswith(".enc")]
def main():
    print("=== Note Encryptor ===")
    while True:
        print("\n1. Write encrypted note\n2. Read note\n3. List notes\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Enter filename (without extension): ").strip()
            note = input("Write your note (single line): ")
            try:
                key = int(input("Enter numeric key (1-255): "))
                if not (1 <= key <= 255): raise ValueError
            except ValueError:
                print("Invalid key.")
                continue
            fname = f"{name}.enc"
            write_encrypted(note, fname, key)
            print(f" Saved & encrypted as {fname}")
        elif choice == "2":
            notes = list_encrypted_notes()
            if not notes:
                print("No encrypted notes found.")
                continue
            for i, n in enumerate(notes, 1):
                print(f"{i}. {n}")
            try:
                sel = int(input("Select note number: ")) - 1
                key = int(input("Enter numeric key: "))
                fname = notes[sel]
            except Exception:
                print("Invalid selection/key.")
                continue
            text = read_encrypted(fname, key)
            if text is None:
                print("Decryption failed — wrong key or corrupted file.")
            else:
                print("\n--- Decrypted Note ---")
                print(text)
                print("----------------------")
        elif choice == "3":
            notes = list_encrypted_notes()
            if notes:
                print("Encrypted notes:")
                for n in notes:
                    print(" -", n)
            else:
                print("No encrypted notes found.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()
