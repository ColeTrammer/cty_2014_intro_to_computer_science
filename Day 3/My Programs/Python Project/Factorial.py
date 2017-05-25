def main():
    a = 0
    c = 1
    while True:
        try:
            a = int(raw_input("Please enter a number."))
            for b in range(1, a):
                c = b * c
            break
        except ValueError:
            ""

    print c
if __name__ == "__main__":
    main()