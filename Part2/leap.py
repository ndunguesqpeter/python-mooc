# Leap year logic: checks if a given year is a leap year
# according to the standard rule (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

# 1. Initialization: get the year from user input and initialize a flag variable
year = int(input("Enter a year to test if it's a leap year [0-3000]: "))
leap_year = False  # assume it's not a leap year by default

# 2. Nested condition: apply the leap year rules
if year % 4 == 0:  # a year is a leap year if it's divisible by 4
    if year % 100 == 0:  # unless it's also divisible by 100
        if year % 400 == 0:  # unless it's also divisible by 400
            leap_year = True  # it's a leap year
        else: 
            leap_year = False  # it's not a leap year
    else:
        leap_year = True  # it's a leap year
else:
    leap_year = False  # it's not a leap year
    
# 3. Output the result
if leap_year:
    print("That's a leap year.")
else:
    print("That's NOT a leap year.")