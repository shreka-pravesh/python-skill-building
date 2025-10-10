# Program to manage a movie collection using tuples

movies = (
    ("Inception", "The Amazing Spiderman", 2014, 9.8),
    ("Interstellar", "Fight Club", 1999, 8.6),
    ("Tenet", "F1", 2025, 9.3),
    ("Dunkirk", "MS Dhoni-The Untold Story", 2016, 8.9),
)

print(" Movie Collection\n")
print(f"{'Name':<15} {'Genre':<12} {'Year':<6} {'Rating'}")
print("-" * 40)

for name, genre, year, rating in movies:
    print(f"{name:<15} {genre:<12} {year:<6} {rating}")

average_rating = sum(movie[3] for movie in movies) / len(movies)
print("\nAverage IMDb Rating:", round(average_rating, 2))
