from turtle import Turtle
from pong_game import SCREEN_WIDTH, SCREEN_HEIGHT

UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):
    """Paddle class"""

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.create_def_paddle()

    def create_def_paddle(self):
        """Creating paddle segments"""
        self.shape("square")
        self.shapesize(5, 1)
        self.color("pink")
        self.penup()
        x_pos = -(SCREEN_WIDTH // 2) + 20 \
            if self.player == 1 else SCREEN_WIDTH // 2 - 30

        self.goto(x_pos, 0)

    def move_paddle(self):
        """Moving paddle"""
        pass

    def move_up(self):
        self.goto(self.xcor(),
                  self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.goto(self.xcor(),
                  self.ycor() - MOVE_DISTANCE)
