from turtle import Turtle
import random

BALL_COLOR = "#ffffff"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.ball_speed = 3
        self.x_move = self.ball_speed
        self.y_move = self.ball_speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1.1
        self.y_move *= 1.1

    def new_round_ball_reverse(self):
        self.x_move *= -1

    def new_round(self):
        self.clear()
        self.x_move = (random.choice([-3, 3]))
        self.y_move = (random.choice([-3, 3]))
        new_y = random.randint(-100, 100)
        self.setpos(0, new_y)
        self.new_round_ball_reverse()
