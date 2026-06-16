code = input("Please type in a password: ")

while True:
    password = input("Please type in a password again: ")
    if password == code:
        break

    print("They do not match!")
    
print("User account created!")