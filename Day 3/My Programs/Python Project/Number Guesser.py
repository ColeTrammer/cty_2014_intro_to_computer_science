def main():
    list2 = []
    for x in range(101):
        list2 += [x]
    x = 0
    num = 0
    a = 50
    b = 0
    c = 0
    while num != 1:
        fifty = raw_input("Is your number greater than " + str(a))
        if fifty == "yes":
            a = (100 + a)/2

        elif fifty == "no":
            a = (100 - a)/2
            c += 1

        elif fifty == "neither":
            num = 1
            print a


if __name__ == "__main__":
    main()