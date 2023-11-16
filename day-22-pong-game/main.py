from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from field import Goal

screen = Screen()
screen.tracer(0)
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("#111111")

scoreboard = Scoreboard()
r_goal = Goal((397, 0))
l_goal = Goal((-407, 0))

left_player_paddle_color = screen.textinput("Color Choice",
"""
LEFT PLAYER

Type in your color, f.e.

• Cyan
• Magenta
• Orange
• Green
""")

right_player_paddle_color = screen.textinput("Color Choice",
"""
RIGHT PLAYER

Type in your color, f.e.

• Cyan
• Magenta
• Orange
• Green
""")

r_paddle = Paddle((350, 0), right_player_paddle_color)
l_paddle = Paddle((-360, 0), left_player_paddle_color)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:

    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect if Left Player scores
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.new_round()

    # Detect if Right Player scores
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.new_round()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
