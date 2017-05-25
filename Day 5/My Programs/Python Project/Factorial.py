def main():
    while True:
        try:
            a = int(raw_input("Please enter a number."))
            for b in range(a):
                 c = a * b

        except ValueError:
            print "Please enter a number."
if __name__ == "__main__":
    main() 