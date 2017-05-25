
"""
Filename: Turtle_One.py


Chris really wants to draw a box. But he can't get the last side =(
Can you finish the box?

"""
import turtle


def main():

    wn = turtle.Screen()     # Make the screen pop up
    Chris = turtle.Turtle()  # Make the turtle in the screen and name it "Chris

    Chris.color("blue")
    Chris.shape("turtle")

    Chris.forward(50)       # Move Chris the turtle froward 50 units
    Chris.left(90)          # Rotate Chris the turtle to the left 90 degrees
    Chris.forward(50)       # Move Chris the turtle froward 50 units
    Chris.left(90)          # Rotate Chris the turtle to the left 90 degrees
    Chris.forward(50)       # Move Chris the turtle froward 90 units
    Chris.left(90)          # Rotate Chris the turtle to the left 50 degrees
    Chris.forward(50)       # Move Chris the turtle froward 90 units


    wn.exitonclick()
if __name__ == "__main__":
    main()
