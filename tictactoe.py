# Tic Tac Toe game

# Before your interview, write a program that lets two humans play a game of Tic Tac Toe in
#  a terminal. The program should let the players take turns to input their moves. 
#  The program should report the outcome of the game.

""" engineering design
    1) welcome to tic tac toe
    2) to start a game, press start 
    3) name the first player 
    4) name the second player 
    5) make player one go (increment game counter)
        -if winner decided with the new move, exit with exiting statement
    6) make player two go (increment game counter)
        -if winner decided with the new move, exit with exiting statement
    8) repeat step 5,6 until game counter == 9 

"""

# During your interview, you will pair on adding support for a computer player to your
#  game. You can start with random moves and make the AI smarter if you have time.

class Player:
    def __init__(self, name):
        self.name = name
        self.moves = []



def play_turn(player, moves): 
    move = input(player.name + ", pick your move: ")
    while move == '':
        print("Please input an option!\n")
        move = input(player.name + ", pick your move: ")

    while int(move) in moves:
        print("Square already taken, please try again!")
        move = input(player.name + ", pick your move: ")

    player.moves.append(int(move))
    player.moves.sort()
    moves.append(int(move))
    return moves

def show_board(): 
    # TODO
    print("hmm this will be interesitng ")


def game_decided(player): 
    # TODO:think about scaling this upto infinitesmal tictactoe
    winning_pairs = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    if player.moves in winning_pairs: 
        return True 
    else: 
        return False


def declare_winner(player):
    print("Congratulations - " + player.name + "won!")


def main(): 

    all_moves = []
    num_turns = 0
    game_over = False
    print("\n \nWelcome to Tic Tac Toe \n")
    start = input("To start a game, type S: ")

    if start != "S":
        print("\nAw, sorry to see you go. Have a great day ahead!\n\n\n\n")
        exit()  

    print("\nAlright, let's get to it!\n")  
    
    #TODO: Cue mario music 
    #get names of player 1/2
    #toss to decide who goes first


    print("So here are the rules: each player picks one box to fill out of the nine boxes here and press the corresponding number. Player 1 is Os and player 2 is Xs \n\n\n")
    print(" _____ _____ _____\n| 1   |  2  |  3  |\n|_____|_____|_____|\n| 4   |  5  |  6  |\n|_____|_____|_____|\n| 7   |  8  |  9  |\n|_____|_____|_____|\n")
    #explain rules and the 9 boxes
    player1 = Player("player1")
    player2 = Player("player2")
    while (num_turns != 9 and not game_over):
        if num_turns % 2 == 0:
            all_moves = play_turn(player1, all_moves)
            num_turns += 1
            if game_decided(player1):
                declare_winner(player1)
                exit()

        else:
            all_moves = play_turn(player2, all_moves)
            num_turns += 1
            if game_decided(player2):
                declare_winner(player2)
                exit()


    print("Oof - this seems like a draw. We got some smart cookies here!")

    """ 
     _____ _____ _____  
    | 1   |  2  |  3  | 
    |_____|_____|_____|
    | 4   |  5  |  6  |
    |_____|_____|_____|
    | 7   |  8  |  9  |
    |_____|_____|_____|
    
    """
if __name__=="__main__": 
    main()
