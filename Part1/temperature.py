#Conversion from Fahrenheit to Celcius Dgree C=[F-32]*(5/9)
#Promt user for Fahrenheit
fahrenheit = int(input("Please type in temperature(F):"))
celcius = (fahrenheit-32)*(5/9)
print(f"{fahrenheit} degrees Fahrenheit equals {celcius} degrees Celsius")
#Condition
if celcius < 0:
    print("Brr!It's cold in here!")
