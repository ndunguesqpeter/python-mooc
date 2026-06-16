# Define a list of items
items = ["a", "b", "c", "d", "e", "f", "g"]

# Loop through the indices of the items list
for i in range(len(items)):
    # Check if the current index is a multiple of 3 (i.e., 0, 3, 6, etc.)
    if i % 3 == 0:
        # If it is, print the item at this index
        print(items[i])