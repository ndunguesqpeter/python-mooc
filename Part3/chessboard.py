def chessboard(length):
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

if __name__ == "__main__":
    chessboard(6)
    #https://claude.ai/share/c213664b-ff9f-4cbc-922f-248eb1adfa4f