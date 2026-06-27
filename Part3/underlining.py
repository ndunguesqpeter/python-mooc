# This is an infinite loop that continues until a certain condition is met
while True:
    # Ask the user to input a string and store it in the 'string' variable
    string = input("Please type in a string: ")
    
    # Check if the input string is empty
    if string == "":
        # If the string is empty, break out of the loop
        break
    
    # Print the input string
    print(string)
    # Print a line of '-' characters that is the same length as the input string to underline it
    print("-" * len(string))