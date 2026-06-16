# Define the maximum number of allowed login attempts
MAX_ATTEMPT = 3

# Set the correct password for login
correct_password = "secret123"

# Initialize a counter for the number of attempts made
attempts = 0

# Enter a loop that continues until a valid password is entered or max attempts are reached
while True:
    # Prompt the user to enter their password and remove leading/trailing whitespace
    password = input("Please enter the password: ").strip()
    
    # Increment the attempt counter
    attempts += 1
    
    # Check if the entered password is correct
    if password == correct_password:
        # If correct, print a success message and exit the loop
        print("Login successful! Welcome.")
        break
    
    # Check if the maximum number of attempts has been reached
    if attempts == MAX_ATTEMPT:
        # If max attempts reached, print an error message and exit the loop
        print("Too many failed attempts.")
        break
    else:
        # If not max attempts, print the number of remaining attempts
        print(f"Incorrect password. {MAX_ATTEMPT - attempts} attempts left.")