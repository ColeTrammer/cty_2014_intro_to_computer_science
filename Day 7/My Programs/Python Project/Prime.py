def main():
    while True:
        try:
            p = int(raw_input("Please enter a number."))
            if p <= 1:
                print "Please enter an integer greater than 1"
                break
            n = 2
            b = 0
            while n < p:
                a = p % n
                n = n + 1
                if a == 0:
                    print "Number is not a prime."
                    break
                else:
                    b = 1
            if b == 1:
                print "prime"
                break
        except ValueError:
            print "Please enter a integer greater than 1"










if __name__ == "__main__":
    main()