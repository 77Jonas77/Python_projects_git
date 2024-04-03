"""Scoreboard class"""
from turtle import Turtle

DATA_SCORE_FILE = 'highest_score.txt'

FONT = ("Arial", 24, "normal")
ALIGEMENT = "center"


class Scoreboard(Turtle):
    """Scoreboard for our snake game"""

    def __init__(self, height):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.highest_score = 0
        self.score = 0
        self.screen_height = height
        self.goto(0, self.screen_height // 2 - 50)
        self.load_highest_score()

    def update_score(self, num_to_add=0):
        self.score = self.score + num_to_add
        self.clear()
        self.write(f"SCORE: {self.score}   HIGHEST SCORE: {self.highest_score}",
                   align=ALIGEMENT, font=FONT)
        self.goto(0, self.screen_height // 2 - 50)

    def check_highest_score(self):
        """Using after round ends"""
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.save_highest_score()
        self.score = 0
        self.update_score(0)

    def load_highest_score(self):
        """Load the highest score"""
        with open(DATA_SCORE_FILE, "r") as f:
            self.highest_score = int(f.read())
            self.update_score(0)

    def save_highest_score(self):
        """Load the highest score"""
        with open(DATA_SCORE_FILE, "w") as f:
            f.write(f"{self.highest_score}")
