# Loop through numbers from 1 to 15 (the upper limit in range() is exclusive)
upper_limit = int(input("Please enter the limit: "))
for num in range(1, upper_limit):
    # Check if the number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        # If so, print "Fizzbuzz"
        print("Fizzbuzz")
    # Check if the number is divisible by 3 but not 5
    elif num % 3 == 0:
        # If so, print "Fizz"
        print("Fizz")
    # Check if the number is divisible by 5 but not 3
    elif num % 5 == 0:
        # If so, print "Buzz"
        print("Buzz")
    # If none of the above conditions are met, print the number itself
    else:
        print(num)