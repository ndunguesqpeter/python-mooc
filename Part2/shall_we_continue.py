# Create an infinite loop that will continue until a break statement is encountered
while True:
    # Print "hi" to the console on each iteration of the loop
    print("hi")
    
    # Prompt the user for input and store their response in the 'answer' variable
    answer = input("Shall we continue? ")
    
    # Check if the user's response is "no"
    if answer == "no":
        # If the response is "no", exit the loop
        break

# This line will be executed once the loop is exited
print("okay then")
        