# Iitialize
is_game_running = True
player_has_key = False

while is_game_running:
    action = input("Do you want to 'search' for the key or 'unlock' the door? ")
    
    if action == "search":
        player_has_key = True
        print("You found the golden key!")
        break
    
    elif action == "unlock":
        if player_has_key:
            print("The door opens! You win!")
            is_game_running = False
        else:
            print("The door is locked. You need a key")
    else:
        print("Invalid action.")