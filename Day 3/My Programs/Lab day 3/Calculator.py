def main():
    a = int(raw_input(" What is your favorite number?"))
    b = int(raw_input(" Give another number you like."))
    z = a + b
    y = a - b
    x = a * b
    w = a/b
    v = a//b
    u = a ** b
    t = a % b

    print " ORDER: ADD, SUB, MULT, DIV, FDIV, EXP, MOD"
    print z
    print y
    print x
    print w
    print v
    print u
    print t


if __name__ == "__main__":
    main()