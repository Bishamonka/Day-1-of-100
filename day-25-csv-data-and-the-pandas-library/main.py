

import turtle
import pandas
from states_manager import LabelMaker

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

list_of_guessed_states = []

while len(list_of_guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(list_of_guessed_states)}/50 States Correct",
                                  prompt="What's another state's name?").title()
    if user_guess == "Exit":
        break
    for row in data.state:
        if row == user_guess and user_guess not in list_of_guessed_states:
            state_name_x_coordinate = int(data[data.state == user_guess].x)
            state_name_y_coordinate = int(data[data.state == user_guess].y)
            list_of_guessed_states.append(user_guess)
            new_state = LabelMaker(user_guess, state_name_x_coordinate, state_name_y_coordinate)

states_to_learn = [state for state in data.state if state not in list_of_guessed_states]
# for state in data.state:
#     if state not in list_of_guessed_states:
#         states_to_learn.append(state)
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
