# Program to track gift distribution during a festival event

invited_guests = {"Vinisha", "Divya", "Darshini", "Shreka", "Deepi", ""}
received_gifts = {"Vinisha", "Divya", "Darshini"}
print(" Invited Guests:", invited_guests)
print(" Guests who received gifts:", received_gifts)
not_received = invited_guests - received_gifts
if not_received:
    print("\n Guests yet to receive gifts:")
    for guest in not_received:
        print("-", guest)
else:
    print("\n All guests have received their gifts!")
