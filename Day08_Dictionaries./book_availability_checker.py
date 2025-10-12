# Program: Book Availability Checker
# Concept: Dictionary lookup

books = {
    "The Alchemist": "Available",
    "1984": "Issued",
    "Python Basics": "Available"
}
book = input("Enter book name: ").title()
if book in books:
    print(f"{book} is {books[book]}")
else:
    print("Book not found in library.")
