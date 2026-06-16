# Define a list of colors
colors = ["red", "blue", "yellow", "green"]

# Continue executing the loop as long as the 'colors' list is not empty
while colors:
    # Remove and return the last element from the 'colors' list
    color = colors.pop(-1)
    # Print a message indicating that the removed color is being processed
    print(f"Processing color: {color}")