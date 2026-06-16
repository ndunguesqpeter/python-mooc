#print a square of character
def squared(s, n):
    #Repeat the string to be at least as long as n * n
    repeated_s = s * ((n * n // len(s)) + 2)
    #Initialize index to keep track of the current position in the repeated string
    index = 0
    row = 0
    while row < n:
        print(repeated_s[index:index + n])
        index += n
        row += 1
        
#Example usage
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)