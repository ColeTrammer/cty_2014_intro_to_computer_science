

class Phone:

    """
    Instantiates a new instance of the Phone class
    """
    def __init__(self, color, square_area, brand, smart):
        self.color = color
        self.square_area = square_area
        self.brand = brand
        self.smart = smart

    """
    Returns a string detailing the phone's attributes
    """
    def __str__(self):
        result = ""
        result += "Phone:\n"
        result += "The color of the phone is " + self.color + ".\n"
        result += "The square area of the phone is " + str(self.square_area) + ".\n"
        result += "The brand of the phone is " + self.brand + ".\n"
        result += "The intelligence of the phone is " + self.smart + ".\n"
        return result

    """
    @self          The reference Phone object
    @new_color     Color to change the phone to

    changes the phone's color
    """
    def change_color(self, new_color):
        self.color = new_color
        print "The new color is " + self.color + "."
    """
    @num           Number that the phone calls

    allows for a phone call
    """
    def phone_call(num1, num):
        print "Dialing " + str(num)
        raw_input()
        print "Hello"
        raw_input()
        print "Bye"
        raw_input()

    """
    @self          The reference Phone object
    @sz            Number to expand the phone by

    expand the size of the phone by sz
    """
    def expand(self, sz):
        self.square_area += sz
        print "The new square area is " + str(self.square_area) + " inches squared."
    """
    @phone1        First phone to compare
    @phone2        Second phone to compare

    compares two phones based on size and smartness
    """
    def compare(phone1, phone2):
        if phone1.smart == "smart" and phone2.smart == "dumb":
            print "Phone1 wins!\n" + str(phone1)
        elif phone2.smart == "smart" and phone1.smart == "dumb":
            print "Phone2 wins!\n" + str(phone2)
        else:
            if phone1.square_area > phone2.square_area:
                print "Phone1 wins!\n" + str(phone1)
            elif phone2.square_area > phone1.square_area:
                print "Phone2 wins!\n" + str(phone2)
            else:
                print "They are very similar!\nThey both win\n" + str(phone1) + "\n" + str(phone2)


def main():
    phone1 = Phone("red", 20, "apple", "smart")
    phone2 = Phone("yellow", 25, "android", "smart")
    phone1.expand(6)
    phone2.change_color("green")
    phone1.phone_call("123-456-7890")
    Phone.compare(phone1, phone2)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()