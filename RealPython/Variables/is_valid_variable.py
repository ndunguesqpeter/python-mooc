import keyword

def is_valid_variable(name):
    # Check whether name is a valid python variable name
    # Check if the variable is a valid Python identifier
    if not name.isidentifier():
        return False
    
    # Check if the name is a reserved key word
    if keyword.iskeyword(name):
        return False
    
    #if the name passes the check, its a valid variable name
    return True
# Example usage
print(is_valid_variable("my_var"))
print(is_valid_variable("for"))
print(is_valid_variable("2fast"))
print(is_valid_variable("total_count"))