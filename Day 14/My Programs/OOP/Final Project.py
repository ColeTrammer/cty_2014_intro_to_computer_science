import random


"""
@dict2   The dictionary indexed starting at 1 to be displayed in a grid

prints the dictionary in a square grid
"""


def display(dict2):
    output = []
    counter = 1
    y = 1
    z = 7
    it = 0
    for x in range(6):
        for i in range(y, z):
            output.append(dict2[i])
            counter += 1
        y += 6
        z += 6
        if z == 37:
            z -= 1
    output.append(dict2[len(dict2)])
    while it <= 35:
        print str(output[it]) + "   " + str(output[it + 1]) + "   " + str(output[it + 2]) + "   " + str(output[it + 3])\
            + "   " + str(output[it + 4]) + "   " + str(output[it + 5] + "        " + str(it + 6) + "\n")
        it += 6


def main():

    """
    Program by Cole to a play a memory game!!!

    Uses dictionaries!!!
    """
    moves_list = []
    print "Welcome to the memory GAME!!!\n"
    games = int(raw_input("How many games do you want to play?"))
    game_counter = 1
    while games >= game_counter:
        board = {}                  # goal of the game is to get
        board_storage = {}          # board_state to = board
        for y in range(1, 37):
            board_storage[y] = "-"  # creates a dictionary 1- 36 with the value "-"
                                         # setup display for the game
        display(board_storage)
        print "The indexes for row 1 are 1 - 6, then 7 - 12 for the second and so on.\n"

        list_number = ["!", "@", "#", "$", "%", "^", "&", "*", "|", "~", "+", "=", "/", "?", ">", "<", ":", "'",
                       "!", "@", "#", "$", "%", "^", "&", "*", "|", "~", "+", "=", "/", "?", ">", "<", ":", "'"]
                                                                                                # list to choose from
        for irrelevant in range(1, 37):                 # random implementation
            store = random.choice(list_number)          # appends the random choice to
            board[irrelevant] = store                   # board, which is the final state
            list_number.remove(store)                   # of the game.

        """
        the loop that takes inputs until the player wins

        hooks up to graphics bad graphics
        """
        moves = 0
        checker = 0                                                         # storing variables
        while True:
            try:
                choice2 = 0
                if board_storage == board:                                  # detects when the game is won
                    break
                if checker != 1:
                    choice1 = int(raw_input("Please enter an index(1)."))     # input choices

                while checker == 0 or checker == 1:
                    if checker == 1:
                        choice2 = int(raw_input("Please enter an index(2)."))  # input choices
                    if checker == 0:
                        if choice1 < 1 or choice1 > 36:                     # error proof [below]
                            print "Not valid."
                            break
                        if board_storage[choice1] == board[choice1]:        # error if choice1 is picked when already up
                            print "Not valid."
                            break
                    if checker == 1:
                        if board_storage[choice2] == board[choice2]:        # error if choice2 is picked when already up
                            print "Not valid."
                            break
                    for asdf in range(1, 37):
                        if choice1 == asdf or choice2 == asdf:              # checks if input matches an index
                            board_storage[asdf] = board[asdf]
                            checker += 1
                            moves += 1                                    # moves count the number of turns taken to win
                            if asdf == choice1:                             # stores choice1 that needs to be reset
                                store_choice1 = choice1
                                choice1 = 0
                            display(board_storage)                          # displays the board state
                            if choice2 > 0:
                                if board[store_choice1] != board[choice2]:  # checks if letters do not match
                                    board_storage[store_choice1] = "-"
                                    board_storage[choice2] = "-"          # replaces number with "-" if they guess wrong

                    if checker == 2:
                        checker = 0
                        break
            except ValueError:                                   # Value Error activates if the user doesn't input a int
                print "Not valid."
        moves_list.append(moves)                                 # stores moves in a list called moves_list
        print "You won in " + str(moves) + " turns!"
        if games == game_counter:
            print str(moves_list) + "\nIs your list of scores starting with the first game played."  # prints the list
        else:                                                                                        # of scores
            time_stall = raw_input("Press any key to play your next game.")    # stalls so user can see their score
        game_counter += 1   # counts games

if __name__ == "__main__":
    main()