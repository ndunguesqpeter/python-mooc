# Program that prints out all even numbers between 2 and 30 (inclusive) using a loop

# Get user input and store it as an integer
num = int(input("Please enter a number: "))

# Continue the loop as long as the number is between 2 and 30 (inclusive)
while 2 <= num <= 30:  # Changed to <= 30 for inclusivity
    # Check if the number is even by verifying if it leaves a remainder when divided by 2
    if num % 2 == 0:
        # Print the even number
        print(num)
    # Increment the number by 1 to move to the next iteration
    num += 1
    