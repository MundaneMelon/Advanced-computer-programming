import turtle
from turtle import *
import random


def main():
    turtle.bgcolor("gray")
    length = 10
    angle = random.randint(90, 180)

    turtle.tracer(50, 0)

    turtle.colormode(255)

    turtle.width(50)
    speed(0)
    penup()
    left(180)
    forward(length / 2)
    left(90)
    forward(length / 2)
    left(90)

    pendown()
    while True:
        f = random.randint(1, 4)
        print(f)
        for i in range(0, 500):
            pencolor(grabColor(f))
            forward(length)
            left(angle)
            length += random.randint(0, 10)

        turtle.setposition(0, 0)
        turtle.setheading(0)
        length = 1
        angle = random.random() * 360
        print(angle)
        turtle.width(random.randint(0, 100))

        clear()


def grabColor(f):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if f == 2:
        r = 0
    elif f == 3:
        g = 0
    elif f == 4:
        b = 0
    return [r, g, b]

    done()

    turtle.update()


if __name__ == "__main__":
    main()
