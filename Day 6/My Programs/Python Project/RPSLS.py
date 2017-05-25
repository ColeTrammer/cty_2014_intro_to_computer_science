import random
"""
@ param b  takes a number to convert to a game value

tells what the computer picks
"""
def output(b):
    if b == 1:
        return "computer: rock"
    elif b == 2:
        return "computer: paper"
    elif b == 3:
        return "computer: scissors"
    elif b == 4:
        return "computer: lizard"
    elif b == 5:
        return "computer: spock"
"""
@ param list2 It is te choices that can be generated

chooses a random element in a list
"""
def computer(list2):

    b = random.choice(list2)
    return b
"""
@param a is person, @ param b is computer
rock = 1, paper = 2, scissors = 3, lizard = 4, spock = 5
Determines whether you win or lose!
"""

def RPSLS(a, b):
    if a == 1 and b == 3 or a == 1 and b == 4 or a == 2 and b == 1 or a == 2 and b == 5 or a == 3 and b == 2 or a == 3 and b == 4 or a == 4 and b == 2 or a == 4 and b == 5 or a == 5 and b == 1 or a == 5 and b == 3:
        return "   YOU WIN!!!"
    elif a == b:
        return "   TIE!!!"
    else:
        return "   YOU LOSE!!!"


def main():
    """
    Program by Cole to play RPSLS!!!
    """
    """
    list of variables
    """
    list_win = [0, 0]
    list_lose = [0, 0]
    list_tie = [0, 0]
    win = 0
    lose = 0
    tie = 0
    count = 0
    a = 0
    list2 = [1, 2, 3, 4, 5]
    """
    user input system

    a represents the person's input
    """
    while True:
        try:
            games = int(raw_input("Please enter the amount of games you want to play."))
            if games <= 0:
                print "Enter a positive number!\n"
            else:
                break
        except ValueError:
            print "Enter an positive number!\n"
    while True:
        try:
            person = str(raw_input("Please enter rock, paper, scissors, lizard, or spock."))
            error = 0
            if person == "rock":
                print "you: rock"
                a = 1
                count += 1
                error += 1
            elif person == "paper":
                print "you: paper"
                a = 2
                count += 1
                error += 1
            elif person == "scissors":
                print "you: scissors"
                a = 3
                count += 1
                error += 1
            elif person == "lizard":
                print "you: lizard"
                a = 4
                count += 1
                error += 1
            elif person == "spock":
                print "you: spock"
                a = 5
                count += 1
                error += 1
            else:
                print "Enter a valid game choice."
            """
            game logic to tell who won the game
            """

            if a > 0 and count <= games and error >= 1:
                b = computer(list2)
                print output(b)
                points = RPSLS(a, b)

                print points
                if points == "   YOU WIN!!!":
                    win += 1
                    list_win.append(win)
                elif points == "   YOU LOSE!!!":
                    lose += 1
                    list_lose.append(lose)
                else:
                    tie += 1
                    list_tie.append(tie)
            """
            Finds the largest value to determine the outcome of the game.

            uses lists to count the score
            """
            if count == games:
                list2 = [list_win[len(list_win) - 1], list_lose[len(list_lose) - 1], list_tie[len(list_tie) - 1]]
                print "\nscore:W/L/T"
                print list2
                if list_win[len(list_win) - 1] > list_lose[len(list_lose) - 1]:
                    print "\nYou win the series!!!\nGood job!"
                elif list_win[len(list_win) - 1] == list_lose[len(list_lose) - 1]:
                    print "\nThe series ends up as a tie"
                else:
                    print "\nSorry, but you lost the series."
                break
        except ValueError:
            print "Enter a valid game choice."



if __name__ == "__main__":
    main()