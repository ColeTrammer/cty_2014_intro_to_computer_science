import turtle


def main():
    wn = turtle.Screen()
    wn.bgcolor("#3300DD")

    tess = turtle.Turtle()
    tess.color("green")
    tess.pensize(3)

    tess.forward(50)
    tess.left(120)
    tess.forward(50)
    wn.exitonclick()


if __name__ == "__main__":
    main()