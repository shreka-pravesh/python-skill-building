class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title):
        self.books.append(title)
        print(f"Book '{title}' added.")
    def show_books(self):
        print("Library Collection:")
        for book in self.books:
            print("-", book)
lib = Library()
lib.add_book("Python Basics")
lib.add_book("OOP Concepts")
lib.show_books()
