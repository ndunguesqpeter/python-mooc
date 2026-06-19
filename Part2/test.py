year = int(input("Year:"))
current = year

     
if (current%4 == 0) and ((current%100 != 0) or (current%400 == 0)):
    print(f"{current} is a leap year.")
    current += 1
    print(f"The new current year is {current}.") 
"""Is the input year itself a leap year?"
     ↓ YES → current = year + 1  (skip it, we want the NEXT one)
     ↓ NO  → current stays as year"""
print(f"{current} is not a leap year.")
while True:
    if (current%4 == 0) and ((current%100 != 0) or (current%400 == 0)):
        print(f"The next leap year after {year} is {current}")
        break
    current += 1
    