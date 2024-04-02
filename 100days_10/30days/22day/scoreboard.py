"""Scoreboard class"""
from turtle import Turtle

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    """Scoreboard for our snake game"""

    def __init__(self, height, player):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.screen_height = height
        self.aligement = "left" if player == 1 else "right"
        self.x_pos = -50 if player == 1 else 50
        self.goto(self.x_pos, self.screen_height // 2 - 50)
        self.update_score()

    def update_score(self, num_to_add=0):
        self.score = self.score + num_to_add
        self.clear()
        self.write(f"{self.score}",
                   align=self.aligement, font=FONT)
        self.goto(self.x_pos, self.screen_height // 2 - 50)
