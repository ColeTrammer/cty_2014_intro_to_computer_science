import turtle


def square(x):
    window = turtle.Screen()
    Chris = turtle.Turtle()
    for i in range(x):
        Chris.forward(20)
        Chris.left(90)

        Chris.forward(20)
        Chris.left(90)

        Chris.forward(20)
        Chris.left(90)

        Chris.forward(20)
        Chris.left(90)

        Chris.penup()
        Chris.forward(40)
        Chris.pendown()

    window.exitonclick()


def box_in_box(x):
    i = 20

    wn = turtle.Screen()
    wn.bgcolor("yellow")

    cole = turtle.Turtle()
    cole.pencolor("red")
    while i <= x:
        cole.forward(i)
        cole.right(90)
        cole.fd(i)
        cole.right(90)
        cole.fd(i)
        cole.right(90)
        cole.forward(i)
        cole.penup()

        cole.forward(20)
        cole.left(90)
        cole.fd(20)
        cole.left(180)

        cole.pendown()
        i += 40


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.right(360/n)


def pattern(t, x):
    for x in range(360/x):
        for i in range(4):
            t.fd(50)
            t.right(90)
            t.fd(50)
            t.right(90)
            t.fd(50)
            t.right(90)
            t.fd(50)
        t.right(x)


def spiral(t, x):
    i = 20
    while i <= 1000:
        t.right(x)
        t.forward(i)
        i += 5


def draw_equilateral_tri(t, sz):
    draw_poly(t, 3, sz)


def star(t, sz):
    for x in range(5):
        for i in range(5):
            t.fd(sz)
            t.right(144)
        t.penup()
        t.fd(350)
        t.right(144)
        t.pendown()


def main():
    wn = turtle.Screen()
    wn.bgcolor("yellow")
    t = turtle.Turtle()
    t.pencolor("red")
    t.pensize(1)
    t.speed(0)
    spiral(t, 89)
    wn.exitonclick()
if __name__ == "__main__":
    main()