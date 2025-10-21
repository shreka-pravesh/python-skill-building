import random, string
def generate_password(length=10):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(all_chars, length))
    return password
def main():
    print("=== Password Generator ===")
    while True:
        try:
            length = int(input("Enter password length (8–20): "))
            if 8 <= length <= 20:
                print("Generated Password:", generate_password(length))
            else:
                print("Length out of range!")
        except ValueError:
            print("Please enter a valid number!")
        if input("Generate again? (y/n): ").lower() != 'y':
            break
if __name__ == "__main__":
    main()
