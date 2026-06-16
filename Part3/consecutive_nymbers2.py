limit = int(input("Limit:"))
start = 1
total = 1
equation = "1"
#Condition
while total < limit:
#Update variables
    start += 1
    total += start
    equation += f" + {start}"
print(f"The consecutive sum: {equation} = {total}")