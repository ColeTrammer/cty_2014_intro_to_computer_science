"""
Filename :Turtle_Five.py

Chris wants to stack some boxes! But it looks like he draws a little too much.
Can you help him ny getting rid of the extra line?

"""
import turtle


def main():
    wn = turtle.Screen()     # Make the screen pop up
    Chris = turtle.Turtle()  # Make the turtle in the screen and name it "Chris"

    Chris.color("Lavender")      # Change Chris' color to blue
    Chris.shape("turtle")    # Change Chris into a turtle

    #Box 1
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(100)
    Chris.right(90)

    #Box 2
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(100)
    Chris.right(90)

    #Box 3
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(100)
    Chris.right(90)

    #Box 4
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.forward(50)
    Chris.right(90)
    Chris.right(90)

    wn.exitonclick()


if __name__ == "__main__":
    main()

