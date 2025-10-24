def encrypt_file(input_file, key):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        encrypted = bytes([b ^ key for b in data])
        with open(input_file + ".enc", "wb") as f:
            f.write(encrypted)
        print(" File encrypted successfully!")
    except FileNotFoundError:
        print(" File not found!")
if __name__ == "__main__":
    file = input("Enter file name to encrypt: ")
    key = int(input("Enter numeric key (1-255): "))
    encrypt_file(file, key)
