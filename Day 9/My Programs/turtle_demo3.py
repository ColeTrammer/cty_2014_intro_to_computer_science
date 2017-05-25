import turtle


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")

    tess.penup()
    size = 20
    for i in range(30):
        tess.stamp()
        size += 3
        tess.forward(size)
        tess.right(24)
    wn.exitonclick()

if __name__ == "__main__":
    main()