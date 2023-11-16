from turtle import Turtle

FONT = ("Arial", 10, "normal")


class LabelMaker(Turtle):
    def __init__(self, state_name, x_coordinate, y_coordinate):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_coordinate, y_coordinate)
        self.write(f"• {state_name}", font=FONT)

