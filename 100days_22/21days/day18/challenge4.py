from turtle import *
import random

directions = [0, 90, 180, 360]


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()

    my_turtle.color(r, g, b)


def move_random():
    change_color()
    my_turtle.setheading(random.choice(directions))
    my_turtle.forward(10)


my_turtle = Turtle()

screen = Screen()
my_turtle.pensize(10)
my_turtle.speed(10)


while True:
    move_random()

screen.exitonclick()
