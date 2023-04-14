import random
from check_win import check_win
from display import display, print_board



# The current state of the board
state = {"1":"_", "2":"_", "3":"_","4":"_", "5":"_", "6":"_","7":"_", "8":"_", "9":"_"}
# Values to test against user input   
validate_input = ["1","2","3","4","5","6","7","8","9"]

# Main game loop
while True:
    # Display the board
    print_board(display)
    # Get user input
    user = input("enter a number")
    # Test user input with while loop
    while True:
        if (user in validate_input):
            break
        else:
             user = input("invalid selection please try again:")
    # Check game state with wile loop
    while True:
        if(state[user] == "_"):
            state[user] = "x"
            display[user] = "x"
            break
        else:
            user = input("Space already taken: ")
    # Check if game is won        
    if(check_win(state)):
        break
    # Computers turn
    while True:
        computer = random.randint(1,9)
        if(state[str(computer)] == "_"):
            state[str(computer)] = "o"
            display[str(computer)] = "o"
            break
    # Final check if game is won  
    if(check_win(state)):
        break
   