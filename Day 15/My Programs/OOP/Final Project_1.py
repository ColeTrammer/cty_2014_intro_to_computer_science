

class Car:

    """
    Instantiates a new instance of the Car class
    """
    def __init__(self, color, square_area, engine_size, brand):
        self.color = color
        self.square_area = square_area
        self.engine_size = engine_size
        self.brand = brand

    """
    Returns a string detailing the car's attributes
    """
    def __str__(self):
        result = ""
        result += "Car:\n"
        result += "The color of the car is " + self.color + "\n"
        result += "The square area of the car is " + str(self.square_area) + "\n"
        result += "The engine size of the car is " + str(self.engine_size) + "\n"
        result += "The brand of the car is " + self.brand + "\n"
        return result

    """
    @self               The reference Car object
    @param new_color    The color the we want to change to

    Changes the current value of self.color to new_color
    """
    def change_color(self, new_color):
        self.color = new_color

    """
    @self                The referenced Car object

    print "VROOM!" self.engine_size times
    """
    def rev_engine(self):
        for x in range(self.engine_size):
            print "VROOM!"

    """
    @self                The referenced Car object

    prints "We're driving!!!!!!"!
    """
    def drive(self):
        print "We're driving!!!!!!!"

    """
    @car1                The first Car object to fight
    @car2                The second Car object to fight

    Two cars will fight in mortal combat
    """
    def fight(car1, car2):
        if car1.square_area > car2.square_area:
            print "Car 1 defeats Car 2 in a fight!"
        elif car2.square_area > car1.square_area:
            print "Car 2 defeats Car 1 in a fight!"
        else:
            print "Car 1 and Car 2 come to a mutual understanding and play Scrabble!"


def main():
    Car_A = Car("Hotpink", 100, 7, "Ford")
    Car_B = Car("Green", 101, 8, "Honda")
    Car.fight(Car_A, Car_B)


if __name__ == "__main__":
    main()