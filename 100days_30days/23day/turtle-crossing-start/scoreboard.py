from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Scoreboard class"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def increase_level(self):
        """Increase the level"""
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def game_over(self):
        """Printing game over"""
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", font=FONT, align="center")

    def reset_scoreboard(self):
        self.level = 0
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")
