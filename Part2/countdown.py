# Prompt the user to enter a number and convert their input to an integer
number = int(input("Please enter a number: "))

# Print a message to indicate the start of the countdown
print("Countdown!")

# Create an infinite loop that will continue until it encounters a break statement
while True:
    # Print the current value of the number variable
    print(number)
    # Decrement the number variable by 1
    number -= 1
    # Check if the number has reached 0
    if number == 0:
        # Break out of the infinite loop when the number reaches 0
        break

# Print a final message after the countdown is complete
print("Now!")