
"""
Filename:Turtle_Three.py
Chris is trying to draw a pentagon (5-sided polygon)

It looks a little odd, can you edit the code so that
each side is the same length?
"""

import turtle


def main():
    wn = turtle.Screen()     # Make the screen pop up
    Chris = turtle.Turtle()  # Make the turtle in the screen and name it "Chris"

    Chris.color("Blue")      # Change Chris' color to blue
    Chris.shape("turtle")    # Change Chris into a turtle

    Chris.left(70)
    Chris.forward(70)
    Chris.left(70)
    Chris.forward(70)
    Chris.left(70)
    Chris.forward(70)
    Chris.left(70)
    Chris.forward(70)
    Chris.left(70)
    Chris.forward(70)

    wn.exitonclick()


if __name__ == "__main__":
    main()
