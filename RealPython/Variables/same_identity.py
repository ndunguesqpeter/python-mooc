def same_identity(obj1, obj2):
    # Check if both objects have the same identity using "is" operator
        return obj1 is obj2
# Example usage
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(same_identity(a, b)) # Output: True
print(same_identity(a, c)) # Output: False