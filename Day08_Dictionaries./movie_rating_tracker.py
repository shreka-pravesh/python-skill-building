# Program: Movie Rating Tracker
# Concept: Dictionary with averages

movies = {"The Amazing Spiderman": [10, 9], "F1": [8, 9]}
print(" Movie Rating Tracker ")
movie = input("Enter movie name: ").title()
rating = int(input("Enter your rating (1-10): "))
if movie in movies:
    movies[movie].append(rating)
else:
    movies[movie] = [rating]
print("\n Updated Movie Ratings:")
for name, ratings in movies.items():
    avg = sum(ratings) / len(ratings)
    print(f"{name}: {avg:.1f}/10")
