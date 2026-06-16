# Import the time module to handle timing-related tasks
import time
# Import the Path class from the pathlib module to handle file paths
from pathlib import Path

# Specify the filename to wait for
filename = Path("hello.txt")

# Print a message indicating that the program is waiting for the file
print(f"Waiting for {filename} to be created...")

# Continuously check if the file exists until it is created
while not filename.exists():
    # Print a message indicating that the file is not found and will retry after a delay
    print("File not found. Retrying in 1 second...")
    # Pause the execution for 1 second before retrying
    time.sleep(1)

# Once the file is found, print a success message
print(f"{filename} found! Proceeding with processing.")

# Open the file in read mode and assign it to the 'file' variable
with open(filename, mode="r") as file:
    # Print a header for the file contents
    print("File contents:")
    # Read and print the contents of the file
    print(file.read())