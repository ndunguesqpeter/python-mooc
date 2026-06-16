# Define a list of contacts, where each contact is a tuple containing name, phone number, and email
contacts = [
    ("Linda", "111-2222-3333", "linda@example.com"),    
    ("Joe", "111-2222-3333", "joe@example.com"),
    ("Lara", "111-2222-3333", "lara@example.com"),
    ("David", "111-2222-3333", "david@example.com"),
    ("Jane", "111-2222-3333", "jane@example.com"),
]

# Iterate over each contact in the list
for name, phone, email in contacts:
    # For each contact, print the phone number followed by the name
    print(phone, name)