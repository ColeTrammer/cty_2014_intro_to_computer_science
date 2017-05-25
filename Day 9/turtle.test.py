import turtle
import random


def main():
    wn = turtle.Screen()

    listrandom = []
    for x in range(360):
        listrandom.append(x)

    name = turtle.Turtle()
    name.color("red")
    name.speed(0)
    name.pensize(1)
    while True:
        degrees = random.choice(listrandom)
        name.forward(10)
        name.left(degrees)
    wn.exitonclick()


if __name__ == "__main__":
    main()