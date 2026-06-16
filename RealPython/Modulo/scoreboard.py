players = ["Player A", "Player B"]

turn = 0
while True:
    print(f"It's {players[turn % 2]}'s turn!")
    action = input("Type 'next' for the next turn or 'quit' to stop: ")
    if action.lower() == 'quit':
        break
    turn += 1