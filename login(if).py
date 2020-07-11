key = {123,222,333}

res = int(input("Enter your password: "))

if res in key:
    print("Logged in.")
else:
    print("Invalid password")