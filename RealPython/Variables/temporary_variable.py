# Define a function to calculate variance
def variance(data, degree_of_freedom=0):
    # Calculate the total number of items in the input data
    number_of_items = len(data)
    
    # Calculate the mean of the input data
    mean = sum(data) / number_of_items
    
    # Calculate the total squared deviation from the mean
    total_square_dev = sum((x - mean) ** 2 for x in data)
    
    # Calculate and return the variance
    # The degree_of_freedom parameter is used to adjust the divisor
    # (e.g., for sample variance, use degree_of_freedom=1)
    return total_square_dev / (number_of_items - degree_of_freedom)

# Example usage: calculate and print the variance of a list of numbers
print(variance([3, 4, 7, 5, 6, 2, 9, 4, 1, 3]))