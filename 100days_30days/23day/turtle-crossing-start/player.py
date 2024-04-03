"""Gracz"""
from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Player (main character) functionality class"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_forward(self):
        """Move forward functionality"""
        self.goto(self.xcor(), self.ycor() + 10)

    def move_to_starting_position(self):
        """Move player to the starting position"""
        self.goto(STARTING_POSITION)

    def check_is_nextlvl(self):
        """Check if player crossed the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
