#rectangle of hashes depending on width choosen
#Initialisation
width = int(input("Width:"))
height = int(input("Height:"))
attempts = 0
while attempts < height:
    print("#"*width)
    attempts += 1