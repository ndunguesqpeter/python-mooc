def check_password(): 
    # Get user input for the password and store it in the 'password' variable
    password = input("Create a password for (8-16 characters): ")
    
    # Calculate the length of the password
    length = len(password)
    
    # Check if the password length is outside the allowed range (8-16 characters)
    if length < 8 or length > 16:
        # Print an error message if the length is not within the allowed range
        print("Password must be between 8 and 16 characters.")
    # Check if the password length is a multiple of 4
    elif length % 4 == 0:
        # Print a success message with a condition (length is a multiple of 4)
        print("Strong password! (length is a multiple of 4)")
    else:
        # Print a success message with the password length
        print(f"Password accepted. Length: {length}")
        
# Call the function to start the password checking process
check_password()