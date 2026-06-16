positive = 0
negative = 0
count = 0
total = 0 
while True:
    number = int(input("Number:"))
    if number == 0:
        break
    count += 1
    total += number
    if number > 0:
        positive += 1
    else:
        negative += 1 
print(f"{positive}")
print(f"{negative}")
print(f"{count}")
print(f"{total}")