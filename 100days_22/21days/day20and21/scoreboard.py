"""Scoreboard class"""
from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGEMENT = "center"


class Scoreboard(Turtle):
    """Scoreboard for our snake game"""

    def __init__(self, height):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.screen_height = height
        self.goto(0, self.screen_height // 2 - 50)
        self.update_score()

    def update_score(self, num_to_add=0):
        self.score = self.score + num_to_add
        self.clear()
        self.write(f"SCORE: {self.score}",
                   align=ALIGEMENT, font=FONT)
        self.goto(0, self.screen_height // 2 - 50)
