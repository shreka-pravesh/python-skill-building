# Program to manage travel wishlists using sets

visited_places = {"Paris", "Goa", "Bali", "Singapore"}
wishlist = {"Iceland", "New York", "Switzerland", "Tokyo", "Goa"}
print(" Places you’ve visited:", visited_places)
print(" Your travel wishlist:", wishlist)
already_visited = visited_places & wishlist
yet_to_visit = wishlist - visited_places
print("\n Already visited from wishlist:", already_visited)
print(" Yet to explore:", yet_to_visit)
wishlist.add("Iceland")
print("\n Updated Wishlist:", wishlist)
