length = int(input("Please enter the length: "))
row = 0

while row < length:
    line = ""
    col = 0
    while col < length:
        if (row + col) % 2 == 0:
            line += "1"
        else:
            line += "0"
        col += 1
    print(line)
    row += 1