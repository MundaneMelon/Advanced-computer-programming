from turtle import *


def main():
    length = 500
    red = 1
    green = 1
    blue = 1
    color("blue")
    speed(0)
    penup()
    left(180)
    forward(length / 2)
    left(90)
    forward(length / 2)
    left(90)

    pendown()
    while True:
        forward(length)
        left(125)
        length += 1

    done()


if __name__ == "__main__":
    main()
