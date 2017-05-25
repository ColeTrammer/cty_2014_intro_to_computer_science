
import turtle


def main():
    wn = turtle.Screen()     # Make the screen pop up
    Chris = turtle.Turtle()  # Make the turtle in the screen and name it "Chris"

    Chris.color("Green")      # Change Chris' color to blue
    Chris.shape("turtle")    # Change Chris into a turtle

    counter = 1

    while counter <= 5:
        Chris.forward(51)
        Chris.right(50)
        counter += 1





    wn.exitonclick()


if __name__ == "__main__":
    main()