from turtle import Turtle

ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(x=0, y=336)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=SCOREBOARD_FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.setpos(0, -22)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
