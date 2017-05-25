def main():
    n = int(raw_input("Give a number."))

    if n % 2 == 0:
        print str(n) + " is even!"

    if n % 2 == 1:
        print str(n) + " is odd!"

if __name__ == "__main__":
    main()