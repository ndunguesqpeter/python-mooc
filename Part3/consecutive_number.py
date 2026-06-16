#Ask user Limit. Calculate total of consecutive numbers until total is at least equal to limit
#initialise
limit = int(input("Limit:"))
start = 1
total = 1
#Condition
while total < limit:
    #Update variables
    start += 1
    total += start
print(total)