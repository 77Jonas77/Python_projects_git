from turtle import *


def move_forward():
    my_turtle.forward(10)


def move_bk():
    my_turtle.back(10)


def move_counterclck():
    my_turtle.setheading(my_turtle.heading()-5)


def move_clck():
    my_turtle.setheading(my_turtle.heading()+5)


def clear_drawing():
    screen.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_turtle = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=move_counterclck)
screen.onkeypress(key="d", fun=move_clck)
screen.onkey(key="s", fun=move_bk)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
