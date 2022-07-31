import random
from turtle import Turtle, Screen

ema = Turtle()

screen = Screen()
screen.colormode(255)

ema.speed(0)


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    color = (r, g, b)
    return color


def circles(loops, circle_quality, is_random_color):
    for _ in range(loops):
        if is_random_color:
            ema.color(random_color())
        ema.circle(100, steps=circle_quality)
        ema.left(360/loops)


circles(32, None, True)
pass
screen.exitonclick()
