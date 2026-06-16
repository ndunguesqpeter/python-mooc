# Import the random module to generate random numbers
import random

# Define a function to check if the current speed exceeds a given limit
def check_speed_limit(limit=80):
    # Read the current speed from the speedometer
    speed = read_speedometer()
    # Check if the current speed exceeds the given limit
    if speed > limit:
        # Print a warning message if the speed limit is exceeded
        print("You are over the speed limit! Slow down.")

# Define a function to simulate a speedometer reading
def read_speedometer():
    # Generate a random speed between 30 and 150 km/h
    speed = random.randint(30, 150)
    # Print the simulated speedometer reading
    print(f"Speedometer reading: {speed} km/h")
    # Return the generated speed
    return speed

# Call the function to check the speed limit with the default limit
check_speed_limit()