from display import print_board, display
def check_win(state):
 
    if(state["1"] == "x" and state["2"] == "x" and state["3"] == "x"):
        print("Player wins")
        print_board(display)
        return True
    elif(state["4"] == "x" and state["5"] == "x" and state["6"] == "x" ):
        print("Player wins")
        print_board(display)
        return True
    elif(state["7"] == "x" and state["8"] == "x" and state["9"] == "x"):
        print("Player wins")
        print_board(display)
        return True
    elif(state["1"] == "x" and state["4"] == "x" and state["7"] == "x"):
        print("Player wins")
        print_board(display)
        return True
    elif(state["2"] == "x" and state["5"] == "x" and state["8"] == "x"):
        print("Player wins")
        print_board(display)
        return True
    elif(state["3"] == "x" and state["6"] == "x" and state["9"] == "x"):
        print("PLayer wins")
        print_board(display)
        return True
    elif(state["1"] == "x" and state["5"] == "x" and state["9"] == "x"):
        print("PLayer wins")
        print_board(display)
        return True
    elif(state["3"] == "x" and state["5"] == "x" and state["7"] == "x"):
        print("PLayer wins")
        print_board(display)
        return True
    elif(state["1"] == "o" and state["2"] == "o" and state["3"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["4"] == "o" and state["5"] == "o" and state["6"] == "o" ):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["7"] == "o" and state["8"] == "o" and state["9"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["1"] == "o" and state["4"] == "o" and state["7"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["2"] == "o" and state["5"] == "o" and state["8"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["3"] == "o" and state["6"] == "o" and state["9"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["1"] == "o" and state["5"] == "o" and state["9"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    elif(state["3"] == "o" and state["5"] == "o" and state["7"] == "o"):
        print("Computer wins")
        print_board(display)
        return True
    else:
        return False