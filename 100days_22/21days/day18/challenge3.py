from turtle import *
import random


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()

    my_turtle.color(r, g, b)


def draw_shape():
    for _ in range(angles):
        my_turtle.forward(angle + 30)
        my_turtle.left(angle)


my_turtle = Turtle()
screen = Screen()

max_angles = 10
min_angles = 3

for angles in range(min_angles, max_angles + 1):
    angle = (360 // angles)
    change_color()
    draw_shape()

screen.exitonclick()
