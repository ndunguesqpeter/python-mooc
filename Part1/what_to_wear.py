# Get the weather forecast from the user
temperature = int(input("What is the weather forecast for tomorrow? Temperature: "))
rain = input("Will it rain (yes/no): ")

# Provide a basic clothing recommendation
print("Wear jeans and a T-shirt")

# Adjust the recommendation based on the temperature
if temperature <= 20:
    # Add a jumper if it's cool
    print("I recommend a jumper as well")

if temperature <= 10:
    # Add a jacket if it's cold
    print("Take a jacket with you")

if temperature <= 5:
    # Recommend warmer clothing if it's very cold
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

# Check if it's going to rain and recommend an umbrella
if rain == "yes":
    print("Don't forget your umbrella!")