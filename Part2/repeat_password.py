# Prompt the user to enter a password and store it in the 'code' variable
code = input("Please type in a password: ")

# Enter a loop that continues until the user enters the correct password
while True:
    # Ask the user to re-enter the password
    password = input("Please type in a password again: ")
    
    # Check if the re-entered password matches the original password
    if password == code:
        # If they match, exit the loop
        break
    
    # If they don't match, print an error message
    print("They do not match!")
    
# Once the loop exits, print a success message
print("User account created!")