from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#333333")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(-100, 220)
        self.write(self.l_score, align="center", font=("Courier", 56, "normal"))
        self.setpos(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 56, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("#CCCCCC")
        self.setpos(0, -30)
        self.write("GAME OVER", align="center", font=("Courier", 56, "normal"))

