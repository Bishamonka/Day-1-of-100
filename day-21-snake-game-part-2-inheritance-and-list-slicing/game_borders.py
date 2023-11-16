from turtle import Turtle

BORDER_COLOR = "#888888"
BORDER_SIZE = 2


class Borders(Turtle):

    def __init__(self):
        super().__init__()
        self.draw_borders()

    def draw_borders(self):
        self.hideturtle()
        self.color(BORDER_COLOR)
        self.fillcolor("red")
        self.pensize(BORDER_SIZE)
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)
