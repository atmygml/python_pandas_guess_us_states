from turtle import Turtle
import turtle
import pandas
from stateboard import Stateboard

states = pandas.read_csv("50_states.csv")
states_list = list(states["state"])
print(states_list)

xy_tuple_raw = states[["x", "y"]].to_records(index=False)
xy_tuple = list(xy_tuple_raw)
print(xy_tuple)

screen = turtle.Screen()
# screen.screensize(800, 500)
screen.setup(width=0.7, height=0.7)
title = "U.S. states Game"
screen.title(title)
image = "blank_states_img.gif"
title_sub = "Guess a state..."

guess_list = []
score = 0
initial_state = True
missing_state_list = []

# screen.bgpic(image)

screen.addshape(image)
turtle.shape(image)

game_is_on = True

while game_is_on:
    state_index = -1
    answer_conv = ""

    if not initial_state:
        title_sub = f" {score} / 50 states guessed."

    answer_state = screen.textinput(title=title_sub, prompt="What is the name of a state?")

    if answer_state:
        pass
    else:
        if answer_state == "":
            pass
        else:
            game_is_on = False

    initial_state = False

    try:
        answer_conv = answer_state.title()
    except:
        answer_conv = ""

    answer_conv = answer_conv.strip()

    for state in states_list:
        if state == answer_conv:
            if state in guess_list:
                print(f"You have already guessed this state {state}.")
                state_index = -2
            else:
                print(f"{answer_conv} is in the list...")
                score += 1
                state_index = states_list.index(state)
                guess_list.append(state)
                print(state_index)
                print(f"The state that you have guessed is {states_list[state_index]}. ")
                title_sub = f" {score} / 50 states guessed."
                w_state = Stateboard()
                w_state.write_state(xy_tuple[state_index], states_list[state_index])
                if score == 50:
                    game_is_on = False

    if state_index == -1:
        print(f"{answer_conv} is NOT in the list...")
        if answer_conv == "Exit":
            game_is_on = False

for state in states_list:
    if state in guess_list:
        pass
    else:
        missing_state_list.append(state)

print(missing_state_list)
states_to_learn = pandas.DataFrame(missing_state_list)
states_to_learn.to_csv("states_to_learn.csv")

turtle.mainloop()
