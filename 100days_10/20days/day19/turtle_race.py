"""Wyscigi zolwi
ale dla max 10
"""

from turtle import *
import random

racing_turtles = []
colors = ["red", "green", "blue", "purple", "orange", "yellow", "cyan", "black",
          "gray", "pink"]


# def create_random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     return r, g, b


def setup_turtles(num_of_racing=5):
    """Creating and setting up the turtles"""

    for i in range(num_of_racing):
        race_turtle = Turtle()
        race_turtle.shape("turtle")
        race_turtle.penup()
        race_turtle.color(colors[i])
        race_turtle.shapesize(2, 2)
        # wiem ze to niezbvt optymalne / uniwersalne
        race_turtle.goto(-400, (
                (
                        window_height() * -1 // 2) + window_height() // num_of_racing) +
                         ((window_height() // num_of_racing) * i))
        race_turtle.pencolor("white")
        race_turtle.pendown()
        racing_turtles.append(race_turtle)

def turtle_race():
    """Turtles race simulator"""
    is_race_on = False
    if user_guess:
        is_race_on = True
    while is_race_on:
        for turtle in racing_turtles:
            turtle.forward(random.randint(1, 20))
        for indx, turtle in enumerate(racing_turtles):
            if turtle.xcor() >= window_width() // 2:
                return indx


screen = Screen()
colormode(255)
screen.setup(1000, 500)
user_guess = textinput(title="Make your bet",
                       prompt="Who's gonna win the race? (color) ")

setup_turtles(1)

winner_turtle = turtle_race()
if colors[winner_turtle] == user_guess.lower():
    textinput(prompt="Congratulations!", title="You won!")
else:
    textinput(prompt="OHHHHHH!", title="You lost!")
screen.bye()
