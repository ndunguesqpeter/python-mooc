#1. Initialization- Setting the initial value(s) of the variable(s) used (*within the condition of the loop*)
#This is performed before the loop is first entered
num = int(input("Type in a number: "))
#2. Condition- Defines how long the loop is to be executed. It is set out at the very beginning of the loop.
#Repeat while the number is less than 10
while num < 10:
    print(num)
#3. Update Within each repetition of the loop, the variables involved in the condition are updated
# Each iteration brings the loop one step closer to its conclusion
# Increment by 1
    num += 1