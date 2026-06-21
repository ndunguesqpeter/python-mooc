# Initialize: Print a message and get a number from the user
print("Are you ready?")
number = int(input("Please type in a number: "))

# Condition: Continue the loop as long as the number is greater than 0
while number > 0:
    # Print the current number
    print(number)
    # Update the number by decrementing it by 1
    number -= 1  

# Print a final message after the loop finishes
print("Now!")