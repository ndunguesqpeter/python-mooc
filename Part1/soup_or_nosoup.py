# Ask the user for their name and store it in the 'name' variable
name = input("Please tell me your name: ")

# Check if the user's name is not "Jerry"
if name != "Jerry":
    # If the name is not "Jerry", ask the user for the number of portions of soup they want
    soup = int(input("how many portions of soup? "))
    # Calculate and print the total cost, assuming each portion costs $5.9
    print(f"The total cost is {soup * 5.9}")
    
# Print a message to indicate that the current user's order is complete
print("Next please!")