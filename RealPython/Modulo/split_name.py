def split_name_rows(name_list, modulus = 3):
    for index, name in enumerate(name_list, start=1):
        print(f"{name:-^15} ", end="")
        if index % modulus == 0:
            print()
    print()
print(split_name_rows(["Picard", "Ricker", "Troi", "Crusher", "Worf", "Data", "La foge"]))