from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
square = (b**2)-(4*a*c)
result =sqrt(square)
d = (-b + result)/(2*a)
e = (b + result)/(2*a)
print(f"The roots are {d} and {e}")