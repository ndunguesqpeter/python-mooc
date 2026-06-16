# Define the number of rows in the pattern
num = int(input("Number: "))

for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(col, end="")
    print("") 
