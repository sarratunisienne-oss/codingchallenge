# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)
# ... write as many functions as you need

def displayNumberPattern():
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")

def checkIfValid(state, num, symbol):
    if(num<1 or num>9):
        return False, state

    if(state[num - 1] == '-'):
        state[num - 1] = symbol
        return True, state
    else:
        return False, state

def display(state):
        print(f'{state[0]} {state[1]} {state[2]}')
        print(f'{state[3]} {state[4]} {state[5]}')
        print(f'{state[6]} {state[7]} {state[8]}')

def checkForWinners(state):
#o
    if(state[0] == 'o' and state[1] == 'o' and state[2] == 'o'):
        print("o is winner")
        return True
    if(state[3] == 'o' and state[4] == 'o' and state[5] == 'o'):
        print("o is winner")
        return True
    if(state[6] == 'o' and state[7] == 'o' and state[8] == 'o'):
        print("o is winner")
        return True
    if(state[0] == 'o' and state[3] == 'o' and state[6] == 'o'):
        print("o is winner")
        return True
    if(state[1] == 'o' and state[4] == 'o' and state[7] == 'o'):
        print("o is winner")
        return True
    if(state[2] == 'o' and state[5] == 'o' and state[8] == 'o'):
        print("o is winner")
        return True
    if(state[0] == 'o' and state[4] == 'o' and state[8] == 'o'):
        print("o is winner")
        return True
    if(state[2] == 'o' and state[4] == 'o' and state[6] == 'o'):
        print("o is winner")
        return True

#x
    if(state[0] == 'x' and state[1] == 'x' and state[2] == 'x'):
        print("x is winner")
        return True
    if(state[3] == 'x' and state[4] == 'x' and state[5] == 'x'):
        print("x is winner")
        return True
    if(state[6] == 'x' and state[7] == 'x' and state[8] == 'x'):
        print("x is winner")
        return True
    if(state[0] == 'x' and state[3] == 'x' and state[6] == 'x'):
        print("x is winner")
        return True
    if(state[1] == 'x' and state[4] == 'x' and state[7] == 'x'):
        print("x is winner")
        return True
    if(state[2] == 'x' and state[5] == 'x' and state[8] == 'x'):
        print("x is winner")
        return True
    if(state[0] == 'x' and state[4] == 'x' and state[8] == 'x'):
        print("x is winner")
        return True
    if(state[2] == 'x' and state[4] == 'x' and state[6] == 'x'):
        print("x is winner")
        return True

    return False

def checkForDraw(state):
    for char in state:
        if(char == '-'):
            return False
    print("There is a draw")
    return True

def checkForDrawSpecial(state):
    count_hyphen = 0
    for char in state:
        if(char == '-'):
            count_hyphen += 1
    if(count_hyphen == 0):
        print("There is a draw")
        return True
    
    #o cannot win
    result_if1 = False
    if((state[0] == 'x' or state[1] == 'x' or state[2] == 'x') and 
    (state[3] == 'x' or state[4] == 'x' or state[5] == 'x') and 
    (state[6] == 'x' or state[7] == 'x' or state[8] == 'x') and
    (state[0] == 'x' or state[3] == 'x' or state[6] == 'x') and 
    (state[1] == 'x' or state[4] == 'x' or state[7] == 'x') and
    (state[2] == 'x' or state[5] == 'x' or state[8] == 'x') and
    (state[0] == 'x' or state[4] == 'x' or state[8] == 'x') and 
    (state[2] == 'x' or state[4] == 'x' or state[6] == 'x')) :
        result_if1 = True

    result_if2 = False
    if((state[0] == 'o' or state[1] == 'o' or state[2] == 'o') and 
    (state[3] == 'o' or state[4] == 'o' or state[5] == 'o') and 
    (state[6] == 'o' or state[7] == 'o' or state[8] == 'o') and
    (state[0] == 'o' or state[3] == 'o' or state[6] == 'o') and 
    (state[1] == 'o' or state[4] == 'o' or state[7] == 'o') and
    (state[2] == 'o' or state[5] == 'o' or state[8] == 'o') and
    (state[0] == 'o' or state[4] == 'o' or state[8] == 'o') and 
    (state[2] == 'o' or state[4] == 'o' or state[6] == 'o')) :
        result_if2 = True
    
    if(result_if1 and result_if2):
        print("There is a draw")
        return True

    
    


def main():
    #print("Hello from main!")
    state = ['-' , '-' , '-' , '-' , '-' , '-' , '-' , '-' , '-']

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    player1Symbol, player2Symbol = 'o', 'o'
    player1Symbol = input("Player 1 choose your symbol, write x or o and press enter: ")
    if (player1Symbol == 'x'):
        pass
    else:
        player2Symbol = 'x'
    print(f'player 1 chose {player1Symbol}, player 2 is {player2Symbol}')

    infinite = 0
    while(infinite<100):
        infinite += 1

        result1_valid = False
        while(result1_valid == False):
            displayNumberPattern()
            number1 = int(input(f"Player 1 {player1Symbol}: Please select a number from above image: "))
            print(" ")
            result1_valid, state = checkIfValid(state, number1, player1Symbol)
            if(not result1_valid):
                print("Invalid input")
        print("current state")
        display(state)
        print(" ")
        if(checkForWinners(state)):
            return
        if(checkForDrawSpecial(state)):
            return 
        
        result2_valid = False
        while(result2_valid == False):
            displayNumberPattern()
            number2 = int(input(f"Player 2 {player2Symbol}: please select a number from above image: "))
            print(" ")
            result2_valid, state = checkIfValid(state, number2, player2Symbol)
            if(not result2_valid):
                print("Invalid input")
        print("current state")
        display(state)
        print(" ")
        if(checkForWinners(state)):
            return
        if(checkForDrawSpecial(state)):
            return 
            #player1turn = input("Pchoose a number from 0-8 : ")


# Tic-tac-toe game
if __name__ == "__main__":
    main()


