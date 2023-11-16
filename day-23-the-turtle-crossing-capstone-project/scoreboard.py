from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.setpos(-285, 265)
        self.color("#333333")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align="left", font=FONT)

    def game_over(self):
        self.setpos(0, -20)
        self.color("#333333")
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 32, "normal"))

