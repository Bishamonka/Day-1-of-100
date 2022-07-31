from turtle import Turtle, Screen

ema = Turtle()
screen = Screen()


def move_forwards():
    ema.forward(10)


def move_backwards():
    ema.backward(10)


def turn_counter_clockwise():
    ema.left(10)


def turn_clockwise():
    ema.right(10)


def clear_drawing():
    ema.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()