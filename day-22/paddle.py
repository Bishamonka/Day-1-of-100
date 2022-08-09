from turtle import Turtle

PADDLE_SIZE = 5  # Size of a paddle = 20px * PADDLE_SIZE
MOVE_DISTANCE = 40
COLORS = ["white", "cyan", "magenta", "orange", "green"]


class Paddle(Turtle):

    def __init__(self, coordinates, color):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.color(color)
        self.setpos(coordinates)
        self.up()
        self.down()

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
