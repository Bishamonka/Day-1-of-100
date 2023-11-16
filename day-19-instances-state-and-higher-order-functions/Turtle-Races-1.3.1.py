from turtle import Turtle, Screen
import random
import time

is_rase_on = False
screen = Screen()
screen.setup(width=800, height=480)
screen.bgcolor("#567d46")
user_bet = screen.textinput(title="MAKE A BET", prompt="""
Which turtle will win the race?

• Red
• Orange
• Yellow
• Green
• Blue
• Purple
""").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# turtle_names = ["Ross", "Susanne", "Russel", "Tyler", "Mortimer", "Fifi"]
y_positions = [60, 36, 12, -12, -36, -60]
all_turtles = []

# Draw a path
path = Turtle()
path.hideturtle()
path.penup()
path.speed('fast')
path.setpos(x=-400, y=0)
path.pensize(200)
path.pencolor("#555555")
path.pendown()
path.setpos(x=400, y=0)

# Draw a finish line
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.setpos(x=320, y=80)
finish_line.pensize(2)
finish_line.pencolor("white")
finish_line.pendown()
finish_line.setpos(x=320, y=-80)

# Write a bunch of text
meta_text = Turtle()
meta_text.hideturtle()
meta_text.color("white")
meta_text.hideturtle()
meta_text.penup()

# Type game name
meta_text.sety(155)
meta_text.write(f"TURTLE RACES", move=False, align='center', font=('Verdana', 28, 'bold'))

# Type version
meta_text.sety(140)
meta_text.write(f"v.1.3.1", move=False, align='center', font=('Verdana', 12, 'normal'))

# Type user's choice
meta_text.sety(-173)
meta_text.write(f"Your turtle: {user_bet.capitalize()}", move=False, align='center', font=('Verdana', 13, 'normal'))

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.setpos(x=-340, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    count_down_text = Turtle()
    count_down_text.hideturtle()
    count_down_text.penup()
    count_down_text.color("white")
    count_down_text.sety(-20)
    for count in range(3, 0, -1):
        count_down_text.write(f"{count}", move=False, align='center', font=('Verdana', 40, 'bold'))
        time.sleep(0.6)
        count_down_text.clear()
    count_down_text.write(f"GO!", move=False, align='center', font=('Verdana', 40, 'bold'))
    time.sleep(0.6)
    count_down_text.clear()

    is_rase_on = True

while is_rase_on:
    for turtle in all_turtles:
        if turtle.xcor() > 300:
            is_rase_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(1, 5)
        attempt_for_boost = random.randint(0, 20)
        boost_distance = 2
        if attempt_for_boost == 20:
            turtle.forward(rand_distance)
            for _ in range(0, 5):
                turtle.forward(boost_distance)
        else:
            turtle.forward(rand_distance)

result_message = Turtle()
result_message.color("white")
result_message.hideturtle()
result_message.penup()
if winning_color == user_bet:
    result_message.sety(-10)
    result_message.write(f"WINNER!", move=False, align='center', font=('Verdana', 24, 'bold'))
    result_message.sety(-30)
    result_message.write(f"\n\n\n{winning_color.capitalize()} won!",
                         move=False, align='center', font=('Verdana', 16, 'normal'))
else:
    result_message.sety(-10)
    result_message.write(f"YOU LOST", move=False, align='center', font=('Verdana', 24, 'bold'))
    result_message.sety(-30)
    result_message.write(f"\n\n\n{winning_color.capitalize()} won!",
                         move=False, align='center', font=('Verdana', 16, 'normal'))


screen.exitonclick()
