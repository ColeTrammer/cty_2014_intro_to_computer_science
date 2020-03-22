import random

"""
@dict2   The dictionary indexed starting at 1 to be displayed in a grid

prints the dictionary in a square grid
"""


def display(dict2):
    # the list converted from a dictionary
    output = []
    counter = 1
    y = 1
    z = 7
    it = 0
    for x in range(6):
        for i in range(y, z):                  # for loop that appends values in the dictionary
            output.append(dict2[i])            # converts dictionary to a list
            counter += 1
        y += 6
        z += 6
        if z == 37:
            z -= 1
    output.append(dict2[len(dict2)])
    while it <= 35:
        print(str(output[it]) + "   " + str(output[it + 1]) + "   " + str(output[it + 2]) + "   " + str(
            output[it + 3]) + "   " + str(output[it + 4]) + "   " + str(output[it + 5] + "        " + str(it + 6) + "\n"))
        # prints the dictionary in a grid
        it += 6


def main():
    """
    Program by Cole to a play a memory game!!!

    Uses dictionaries!!!
    """

    moves_list = []
    print("Welcome to the memory GAME!!!\n")
    while True:
        try:
            games = int(input("How many games do you want to play?"))
            if games <= 0:
                print("Please enter a positive integer!")
            else:
                break
        except ValueError:
            print("really...")
    game_counter = 1
    while games >= game_counter:
        board = {}                  # goal of the game is to get
        board_storage = {}          # board_state to == board
        for y in range(1, 37):
            # creates a dictionary 1- 36 with the value "-"
            board_storage[y] = "-"
            # setup display for the game
        display(board_storage)
        print("The indexes for row 1 are 1 - 6, then 7 - 12 for the second and so on.\n")

        list_number = ["!", "@", "#", "$", "%", "^", "&", "*", "|", "~", "+", "=", "/", "?", ">", "<", ":", "'",
                       "!", "@", "#", "$", "%", "^", "&", "*", "|", "~", "+", "=", "/", "?", ">", "<", ":", "'"]
        # list to choose from
        for irrelevant in range(1, 37):                 # random implementation
            # appends the random choice to
            store = random.choice(list_number)
            # board, which is the final state
            board[irrelevant] = store
            list_number.remove(store)                   # of the game.

        """
        the loop that takes inputs until the player wins

        hooks up to graphics bad graphics
        """
        moves = 0
        # storing variables
        checker = 0
        while True:
            try:
                choice2 = 0
                if board_storage == board:                                  # detects when the game is won
                    break
                if checker != 1:
                    # input choices(1)
                    choice1 = int(input("Please enter an index(1)."))

                while checker == 0 or checker == 1:
                    if checker == 1:
                        # input choices(2)
                        choice2 = int(input("Please enter an index(2)."))
                    if checker == 0:
                        # error proof [below]
                        if choice1 < 1 or choice1 > 36:
                            print("Not valid.")
                            break
                        # error if choice1 is picked when already up
                        if board_storage[choice1] == board[choice1]:
                            print("Not valid.")
                            break
                    if checker == 1:
                        # error if choice2 is picked when already up
                        if board_storage[choice2] == board[choice2]:
                            print("Not valid.")
                            break
                    for asdf in range(1, 37):
                        if choice1 == asdf or choice2 == asdf:              # checks if input matches an index
                            board_storage[asdf] = board[asdf]
                            checker += 1
                            # moves count the number of turns taken to win
                            moves += 1
                            if asdf == choice1:                             # stores choice1 that needs to be reset
                                store_choice1 = choice1
                                choice1 = 0
                            # displays the board state
                            display(board_storage)
                            if choice2 > 0:
                                # checks if letters do not match
                                if board[store_choice1] != board[choice2]:
                                    board_storage[store_choice1] = "-"
                                    # replaces number with "-" if they guess wrong
                                    board_storage[choice2] = "-"

                    if checker == 2:
                        checker = 0
                        break
            except:                                   # Value Error activates if the user doesn't input a int
                print("Not valid.")
        # stores moves in a list called moves_list
        moves_list.append(moves/2)
        print("You won in " + str(moves/2) + " turns!")
        if games == game_counter:
            # prints the list
            print(str(moves_list) +
                  "\nIs your list of scores starting with the first game played.")
            break
        variable = input("Do you want to see your scores?")
        # asks if they want to see
        if variable == "yes":
            # their score
            print(str(moves_list))
            # stalls so they can see score
            asdfasdfjfldskjklsfs = input("Press enter to play again")
        game_counter += 1   # counts games


if __name__ == "__main__":
    main()
