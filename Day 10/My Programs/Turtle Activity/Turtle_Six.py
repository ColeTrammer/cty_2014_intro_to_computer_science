"""
Filename: Turtle_Six.py

Chris is trying to draw a star using an iterative statement (A statement that executes multiple times)

He's trying to draw a star. But its not working =(

Help him by fixing his code.
"""

import turtle


def main():
    wn = turtle.Screen()     # Make the screen pop up
    Chris = turtle.Turtle()  # Make the turtle in the screen and name it "Chris"

    Chris.color("Green")      # Change Chris' color to blue
    Chris.shape("turtle")    # Change Chris into a turtle

    counter = 1

    while counter <= 5:
        Chris.forward(100)
        Chris.right(145)
        counter += 1

    wn.exitonclick()


if __name__ == "__main__":
    main()