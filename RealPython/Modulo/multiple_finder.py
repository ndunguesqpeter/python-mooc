def find_multiples():
    # Ask the user to input a number and convert it to an integer
    num = int(input("Enter a number: "))
    # Ask the user to input the upper limit and convert it to an integer
    limit = int(input("Up to what number: "))
    
    # Print a message indicating what the following output represents
    print(f"Multiples of {num} up to {limit}:")
    # Loop over the multiples of num up to limit (inclusive)
    for i in range(num, limit + 1, num):  # Start from num and increment by num
        # Print the multiple followed by a space (without a newline)
        print(i, end=" ")
            
# Call the function to start the program
find_multiples()