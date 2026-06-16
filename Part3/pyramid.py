#Pyramid
#initialise
n = 10 #int(input("Please enter the no. of n:"))
row = "+"
#Condition
while n > 0:
    #print(row)
    #print(f"The numbers of n is:{n}")
    print(" " * n + row)
#Update variables
    row += "++"
    n -= 1