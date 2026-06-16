# FizzBuzz game: prints "Fizz", "Buzz", or "FizzBuzz" based on the input number
# Get user input and convert it to an integer
num = int(input("Number: "))

# Check if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    # If divisible by both, print "FizzBuzz"
    print("FizzBuzz")
# Check if the number is divisible by 3 but not 5
elif num % 3 == 0:
    # If divisible by 3, print "Fizz"
    print("Fizz")
# Check if the number is divisible by 5 but not 3
elif num % 5 == 0:
    # If divisible by 5, print "Buzz"
    print("Buzz")
# Note: numbers not divisible by either 3 or 5 will not print anything