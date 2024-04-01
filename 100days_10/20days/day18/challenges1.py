import turtle
from turtle import Turtle, Screen
# from turtle import *

my_turtle = Turtle()
screen = Screen()

# for _ in range(4):
#     for _ in range(4):
#         turtle.pencolor("Black")
#         turtle.forward(20)
#         turtle.pencolor("White")
#         turtle.forward(20)
#     turtle.right(90)

for _ in range(4):
    for _ in range(4):
        turtle.forward(20)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
    turtle.right(90)

screen.exitonclick()
