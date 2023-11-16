# Create the Player Behavior
# Create the Car Behavior
# Detect collision Turtle with a Car
# Detect when the player has reached the other side
# Add Scoreboard and Game Over

from turtle import Screen
from player_character import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.sety(-280)
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
