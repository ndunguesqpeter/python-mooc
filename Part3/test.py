char = "#"
width = int(input("Width: "))
height = int(input("Height: "))
attempts = 0
while attempts < height:
    print(char*width, end=" ")
    attempts += 1