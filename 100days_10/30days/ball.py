from turtle import *

BALL_MOVE_DISTANCE = 20


class Ball(Turtle):
    """Ball class"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        """Move the ball"""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        """Check if the ball touched the wall"""
        self.y_move *= -1

    def bounce_x(self):
        """bounce the ball after being touched by a paddle"""
        self.x_move *= -1
