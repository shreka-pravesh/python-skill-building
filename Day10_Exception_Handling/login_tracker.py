# Login attempt limiter using exceptions

user, pwd = "admin", "1234"
for attempt in range(3):
    try:
        u = input("Username: ")
        p = input("Password: ")
        if u == user and p == pwd:
            print(" Login Successful!")
            break
        else:
            raise ValueError("Incorrect credentials!")
    except ValueError as e:
        print(e)
else:
    print(" Too many failed attempts. Try later.")
