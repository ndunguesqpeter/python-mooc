# Get user input and store it in a variable
input_string = input("Please enter a word or sentence: ")

# Continuously ask the user to search for a substring
while True:
    # Ask the user for a substring to search for
    substring = input("What are you looking for? ")
    
    # Use the find method to get the index of the substring
    index = input_string.find(substring)
    
    # Check if the substring was found
    if index != -1:  # find() returns -1 if not found
        # If found, print the index
        print(f"Found it at the index {index}")
    else:
        # If not found, print a message and exit the loop
        print("Not found.")
        break