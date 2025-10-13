# Program: Feedback Collector
# Concept: File handling with feedback input and appending

filename = "feedback.txt"
while True:
    print("\n1. Give Feedback\n2. View Feedback\n3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        fb = input("Enter your feedback: ")
        with open(filename, "a") as f:
            f.write(fb + "\n")
        print(" Feedback saved. Thank you!")
    elif choice == "2":
        try:
            with open(filename, "r") as f:
                print("\n All Feedbacks:\n" + f.read())
        except FileNotFoundError:
            print("No feedbacks yet.")
    elif choice == "3":
        print(" Exiting Feedback Collector.")
        break
    else:
        print("Invalid choice, try again.")
