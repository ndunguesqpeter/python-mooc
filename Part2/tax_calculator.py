# Calculator to determine the tax on a gift based on its value

# Get the value of the gift from the user
value = int(input("Value of gift: "))

# Determine the tax based on the gift's value using a nested if-elif-else statement
if value < 5000:
    # Gifts worth less than 5000 euros are tax-free
    tax = 0
elif value <= 25000:
    # Calculate tax for gifts worth between 5000 and 25000 euros
    tax = (100 + (value - 5000) * 0.08)
elif value <= 55000:
    # Calculate tax for gifts worth between 25000 and 55000 euros
    tax = (1700 + (value - 25000) * 0.1)
elif value <= 200000:
    # Calculate tax for gifts worth between 55000 and 200000 euros
    tax = (4700 + (value - 55000) * 0.12)
elif value <= 1000000:
    # Calculate tax for gifts worth between 200000 and 1000000 euros
    tax = (22100 + (value - 200000) * 0.15)
else:
    # Calculate tax for gifts worth over 1000000 euros
    tax = (142100 + (value - 1000000) * 0.17)

# Print the calculated tax or a message if the gift is tax-free
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")