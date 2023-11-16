import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_borders import Borders

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#171717")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
borders = Borders()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_point()
        snake.extend()

    # Detect collision with Walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with Tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
