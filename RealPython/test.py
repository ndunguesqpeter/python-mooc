# Define the number of rows in the pattern
num = 3 

for row in range(num, 0, -1):
    for col in range(1, row + 1):
        print(num - row + 1, end=" ")
    print()
    
    