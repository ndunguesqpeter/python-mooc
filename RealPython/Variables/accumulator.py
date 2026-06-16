# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize variables to accumulate the sum and count of even numbers
accumulator = 0  # store the sum of even numbers
counter = 0  # count the number of even numbers

# Iterate over each number in the list
for number in numbers:
    # Check if the current number is even
    if number % 2 == 0:
        # Increment the count and sum of even numbers
        counter += 1 
        accumulator += number

# Print the sum of even numbers (not the sum of the list, despite the misleading message)
print(f"The sum of the list is {accumulator}")