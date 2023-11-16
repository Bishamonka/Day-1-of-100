from turtle import Turtle
import random

COLORS = ["light slate gray", "gainsboro", "steel blue", "light sky blue", "dark slate gray", "red", "gold"]
STARTING_MOVE_DISTANCE = 0.5
MOVE_INCREMENT = 0.2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.random_chance = 30

    def create_car(self):
        dice_roll = random.randint(1, self.random_chance)
        if dice_roll == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.x_cor = 320
            new_car.y_cor = random.randint(-250, 250)
            new_car.setpos(new_car.x_cor, new_car.y_cor)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.cars_speed)

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT
        self.random_chance -= 1
