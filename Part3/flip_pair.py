#Ask user for an input
num = int(input("Please type in a number: "))

#Initialize a counter variable
i = 1
#loop through the numbers 1 to num
while i <= num:
    #check if current num is (even)
    if i + 1 <= num:
        #print current even num
        print(i + 1)
        #print previous num (odd)
        print(i)
        #increment the counter by 2
        i += 2
    else:
        #if current number is odd and it's the last number print it
        print(i)
        #Increment the counter by 1 to check the next number in the next iteration
        i += 1