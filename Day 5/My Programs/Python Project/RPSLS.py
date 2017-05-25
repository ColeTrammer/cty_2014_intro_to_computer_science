def RPSLS(a):
def main():
    count = 0
    run = 0
    while True:
        try:
            person = str(raw_input("Please enter rock, paper, scissors, lizard, or spock."))
            if person == "rock":
                print "rock"
                a = 1
                count += 1
                run += 1
            elif person == "paper":
                print "paper"
                a = 2
                count += 1
                run += 1
            elif person == "scissors":
                print "scissors"
                a = 3
                count += 1
                run += 1
            elif person == "lizard":
                print "lizard"
                a = 4
                count += 1
                run += 1
            elif person == "spock":
                print "spock"
                a = 5
                count += 1
                run += 1
            else:
                print "Please enter rock, paper, scissors, lizard, or spock."
        except ValueError:
            print "Please enter rock, paper, scissors, lizard, or spock."



if __name__ == "__main__":
    main()