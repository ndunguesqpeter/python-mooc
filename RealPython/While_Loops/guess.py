# Import a function from the random module to generate a random integer
from random import randint

# Define the range for the secret number
LOW, HIGH = 1, 10

# Generate a random secret number within the defined range
secret_number = randint(LOW, HIGH)

# Initialize an empty clue to help the user guess the secret number
clue = ""

# Loop indefinitely until the user guesses the secret number
while True:
    # Prompt the user to guess a number and display the current clue
    guess = input(f"Guess a number between {LOW} and {HIGH}:  {clue}")
    
    # Convert the user's guess to an integer
    number = int(guess)
    
    # Check if the guess is higher or lower than the secret number and update the clue
    if number > secret_number:
        # The secret number is less than the guess, so update the clue accordingly
        clue = f"(less than {number})"
    elif number < secret_number:
        # The secret number is greater than the guess, so update the clue accordingly
        clue = f"(greater than {number})"
    else:
        # The guess matches the secret number, so exit the loop
        break

# Print a success message with the guessed number
print(f"You guessed it! The secret number is {number}")