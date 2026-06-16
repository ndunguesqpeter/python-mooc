def custom_reversed(sequence):
    index = len(sequence) - 1
    while index >= 0:
        yield sequence[index]
        index -= 1
print(list(custom_reversed("12345")))  