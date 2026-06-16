# Initialize a counter to keep track of the number of strings encountered
str_counter = 0
# Iterate over a tuple containing a mix of data types
for item in ("Alice", 10, "Program", None, True, "Ven", "Yoh"):
    # Check if the current item is a string
    if isinstance(item, str):
        # Increment the counter if the item is a string
        str_counter += 1
         # Print the current count and the string
        print(str_counter, "-", item)