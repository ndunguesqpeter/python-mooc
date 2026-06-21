# Define a list of color names
colors = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]

# Use enumerate to loop over the list with both index and value
# The 'start=1' argument makes the index start from 1 instead of 0
for item, code in enumerate(colors, start=1):
    # Print the index (item) and the corresponding color name (code)
    print(item, code)