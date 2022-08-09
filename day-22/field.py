from turtle import Turtle


class Goal(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=30, stretch_len=4)
        self.color("#222222")
        self.setpos(position)
