#Ask user for a number
num = int(input("Please type in a number: "))
#print numbers from 1 to n, alternating between the two ends.
low = 1
high = num
while low <= high:
    print(low)
    if low != high: #Avoid printing the same number twice
        print(high)
    low += 1
    high -= 1