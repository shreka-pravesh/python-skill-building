def decrypt_file(encrypted_file, key):
    try:
        with open(encrypted_file, "rb") as f:
            data = f.read()
        decrypted = bytes([b ^ key for b in data])
        output = encrypted_file.replace(".enc", "_decrypted.txt")
        with open(output, "wb") as f:
            f.write(decrypted)
        print(f" Decryption complete! Saved as {output}")
    except FileNotFoundError:
        print(" Encrypted file not found!")
if __name__ == "__main__":
    file = input("Enter encrypted file name: ")
    key = int(input("Enter the same numeric key: "))
    decrypt_file(file, key)
