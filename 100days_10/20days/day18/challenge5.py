from turtle import *
import random

directions = [0, 90, 180, 360]


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()

    my_turtle.color(r, g, b)


def draw_circle():
    change_color()
    my_turtle.circle(50)
    curr_head = my_turtle.heading()
    my_turtle.setheading(curr_head + 20)


my_turtle = Turtle()

screen = Screen()
my_turtle.pensize(10)
my_turtle.speed(10)
tilt_circle = 20


for _ in range(360 // tilt_circle):
    draw_circle()

screen.exitonclick()
