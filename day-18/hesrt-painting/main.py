# import colorgram
#
# extracted_colors = []
# colors = colorgram.extract('image.jpg', 12)
# for color_object in colors:
#     r = color_object.rgb.r
#     g = color_object.rgb.g
#     b = color_object.rgb.b
#     new_color = (r, g, b)
#     extracted_colors.append(new_color)
# print(extracted_colors)

import random
from turtle import Turtle, Screen

color_list = [(154, 63, 50), (25, 34, 56), (58, 88, 244), (237, 62, 53),
              (133, 69, 91), (55, 27, 39), (206, 140, 160), (59, 33, 27)]

sara = Turtle()
screen = Screen()
screen.colormode(255)

# Dot = 20px (though it's still '0px' size)
# Gap = 50px (but it has to be 'Dot + Gap', so 70px)
# Canvas size 650x650

screen.bgcolor('#f3f3f3')
sara.speed(0)
sara.penup()
sara.hideturtle()

# Canvas Size / 2 = 325
# 10px is a Dot radius so starting point is '-315'
x = -315
y = -315
sara.setx(x)
sara.sety(y)

for _ in range(10):
    for _ in range(10):
        sara.dot(20, random.choice(color_list))
        sara.forward(70)
    y += 70
    sara.setx(x)
    sara.sety(y)
sara.home()
screen.exitonclick()
