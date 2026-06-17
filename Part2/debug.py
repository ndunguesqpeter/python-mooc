# Initialize a counter to track the number of attempts
attempts = 0

# Enter an infinite loop that will be terminated when a condition is met
while True:
    print("Beginning of the while block: ")
    # Prompt the user to input their PIN
    code = input("Please type in your PIN: ")
    # Increment the attempts counter
    attempts += 1
    
    # Print the current number of attempts for debugging purposes
    print("Attempts:", attempts)
    # Print a condition check for debugging purposes
    print("Condition1:", attempts == 3)
    # Check if the number of attempts has reached the maximum allowed (3)
    if attempts == 3:
        # If so, set success to False and exit the loop
        success = False
        break  # Exit the loop

    # Print the entered PIN for debugging purposes
    print("Code:", code)
    # Print another condition check for debugging purposes
    print("Condition2:", code == "1234")
    # Check if the entered PIN is correct
    if code == "1234":
        # If so, set success to True and exit the loop
        success = True
        break  # Exit the loop

    # Inform the user that their PIN is incorrect
    print("Incorrect...try again")

# Check the success status after exiting the loop
if success:
    # If the PIN was entered correctly, print a success message
    print("Correct PIN entered!")
else:
    # If the maximum attempts were reached without success, print a failure message
    print("Too many attempts...")