# Define a function named greet that takes two parameters: name and verbose.
# The verbose parameter is optional and defaults to False if not provided.
def greet(name, verbose=False):
    # Check if the verbose parameter is True.
    if verbose:
        # If verbose is True, print a more detailed greeting message.
        print(f"Hello, {name}! it's great to see you.")
    else:
        # If verbose is False, print a simple greeting message.
        print(f"Hello, {name}!")

# Call the greet function with the name "Pythonista" and default verbosity (False).
greet("Pythonista")
# Call the greet function with the name "Pythonista" and verbosity set to True.
greet("Pythonista", verbose=True)