def main():
    while True:
        try:
            year = int(raw_input ("Please enter a year."))
            a = year % 4
            if a == 0:
                print "leap year"
            else:
                print "Not a leap year"
                break
            break
        except ValueError:
            print "Please enter an integer."




if __name__ == "__main__":
    main()
