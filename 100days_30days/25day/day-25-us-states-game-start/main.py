import turtle

import pandas

screen = turtle.Screen()
screen.title("States Game")

img = "blank_states_img.gif"
turtle.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = len(data)
correct_answers = 0
states_list = data.to_dict()
guessed_states = []

game_on = True
while game_on:
    answer_state = turtle.textinput(
        f"Correct states: {correct_answers}/{all_states}",
        "Give another state name")
    if answer_state == "exit":
        missing_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states_list if
                          state not in guessed_states]
        not_answered_states = pandas.DataFrame(missing_states)
        not_answered_states.to_csv("missing_states.csv")
    break

if answer_state.title() in states_list['state'].values():
    x = int(data[data.state == answer_state.title()].x)
    y = int(data[data.state == answer_state.title()].y)
    state_text = turtle.Turtle()
    state_text.hideturtle()
    state_text.penup()
    state_text.goto(x, y)
    state_text.write(f"{answer_state}")
    correct_answers += 1
    guessed_states.append(answer_state)
if correct_answers == all_states:
    game_on = False
