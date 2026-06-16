# Function takes an int arg, print square of hashes and specific length
def hash_square(length):
    attempts = 0
    while attempts < length:
        print("#" * length)
        attempts += 1

if __name__  == "__main__":
    hash_square(3)
    hash_square(8)