from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.sety(-280)

    def move(self):
        self.forward(10)
