import turtle

import colorgram
from turtle import *
import random

colors = colorgram.extract('image.jpg', 30)


def change_color(data):
    r = data.rgb.r
    g = data.rgb.g
    b = data.rgb.b
    return r, g, b


def draw_painting():
    step = screen.window_width() // 10
    for i in range(10):
        if i != 0:
            penup()
            my_turtle.teleport(-400, my_turtle.pos()[1] + step)
            pendown()
        for _ in range(10):
            my_turtle.dot(20, change_color(random.choice(colors)))

            # my_turtle.fillcolor()
            penup()
            my_turtle.teleport(my_turtle.pos()[0] + step, my_turtle.pos()[1])
            pendown()


my_turtle = Turtle()
screen = Screen()
screen.screensize()

my_turtle.penup()
my_turtle.teleport(-400, -400)
my_turtle.pendown()
my_turtle.speed(11)
colormode(255)

draw_painting()

screen.exitonclick()
