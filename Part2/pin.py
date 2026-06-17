# Define the maximum number of attempts allowed to enter the PIN
max_attempts = 3
# Initialize a counter to track the number of attempts made
attempts = 0

# Continue to prompt the user for their PIN until they reach the maximum attempts
while attempts < max_attempts:
    # Ask the user to enter their PIN
    code = input("Please type in your PIN: ")
    # Check if the entered PIN is correct
    if code == "1234":
        # If the PIN is correct, print a success message and exit the loop
        print("Correct PIN entered!")
        break
    # Increment the attempts counter if the PIN is incorrect
    attempts += 1  
    # Inform the user that their PIN was incorrect and prompt them to try again
    print("Incorrect...try again")
else:
    # This block is executed if the loop completes without breaking (i.e., too many attempts)
    print("Too many attempts...")