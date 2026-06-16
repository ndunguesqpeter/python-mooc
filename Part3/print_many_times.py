#Takes a string and an integer as arguments.
#The integer arg specifies how my times the str arg should be printed
def print_many_times(text, times):
    i = 1
    while 1 <= times:
        print(text)
        times -= 1

if __name__ == "__main__":
    print_many_times( "python", 5)
    print_many_times("kuku", 10)