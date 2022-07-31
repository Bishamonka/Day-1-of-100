import random
from turtle import Turtle, Screen

ema = Turtle()

screen = Screen()
screen.colormode(255)

ema.speed(0)
ema.color("black")


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]


def random_path(loops, step_length, pensize):
    for _ in range(loops):
        ema.pensize(pensize)
        ema.color(random_color())
        ema.setheading(random.choice(directions))
        ema.forward(step_length)


random_path(100, 30, 15)
screen.exitonclick()
