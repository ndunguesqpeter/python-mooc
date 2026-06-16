# Define a list of day abbreviations in order
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Initialize the current day as Saturday (index 5)
current_day = 5
# Specify the number of days to offset from the current day
offset = 3

# Calculate the new day by adding the offset to the current day and taking the modulus of 7
# to wrap around the list of days if necessary
new_day = days[(current_day + offset) % 7]

# Print the resulting new day
print(new_day)