class Movie:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats
    def book_ticket(self, num):
        if num <= self.seats:
            self.seats -= num
            print(f"Booked {num} seat(s). Seats left: {self.seats}")
        else:
            print("Not enough seats available!")
movie1 = Movie("The Amazing Spiderman", 5)
movie1.book_ticket(2)
movie1.book_ticket(4)
