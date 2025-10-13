# Save custom messages from multiple users

name = input("Your name: ")
msg = input("Message: ")
with open("messages.txt", "a") as f:
    f.write(f"{name}: {msg}\n")
print("Message saved successfully!")
