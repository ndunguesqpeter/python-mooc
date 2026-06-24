row = int(input("Rows: "))
intial = 1
while intial <= row:
    column = 1
    while column <= intial:
        print(column, end=" ")
        column += 1
    print()
    intial += 1