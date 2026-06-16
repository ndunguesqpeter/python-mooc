# import time 
import random

# Define a function to simulate reading temperature
def read_temperature():
    # Return a random floating-point number between 20.0 and 30.0
    return random.uniform(20.0, 30.0)

# Create an infinite loop to continuously monitor temperature
while True:
    # Call the read_temperature function to get the current temperature
    temp = read_temperature()
    # Print the temperature with two decimal places
    print(f"Temperature: {temp:.2f}C")
    
    # Check if the temperature has reached 28 degrees or more
    if temp >= 28:
        # If the temperature is high enough, print a message and exit the loop
        print("Requires temperature reached! Stopping monitoring.")
        break
    
    # The original code used time.sleep(1) to pause for 1 second, but time is not available
    # We can use a simple busy-wait loop as a replacement, but it's not efficient
    # A better solution would be to find an alternative to time.sleep or restructure the code
    # For demonstration, we'll just remove this line for now
    # time.sleep(1)