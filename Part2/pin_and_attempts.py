#the order of conditional stmts matters alot
# Initialize the attempts counter to 0
attempts = 0

# Loop indefinitely until the correct PIN is entered
while True:
    # Prompt the user to enter a PIN
    pin = input("PIN: ")
    # Increment the attempts counter
    attempts += 1
    
    # Check if the entered PIN is correct
    if pin == "4321":
        # Break the loop if the PIN is correct
        break 
    # Print an error message if the PIN is incorrect
    print("Wrong")    

# Check the number of attempts and print the corresponding success message
if attempts == 1:
    # Print a special message for a single attempt
    print("Correct! It only took you one single attempt!")
else:
    # Print a generic message for multiple attempts
    print(f"Correct! It took you {attempts} attempts")