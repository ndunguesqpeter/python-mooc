#This is a global variable
name = "Betty"

def hello(given_name):
    #using the global variabble instead of parameters by mistake.
    print("Hello", name)

hello("Steve")
hello("Betty")