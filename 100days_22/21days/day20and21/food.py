"""Food class for snake"""
from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.screen_width = width
        self.screen_height = height
        self.speed("fastest")
        self.food_eaten()
        self.screen_width = width - 50
        self.screen_height = height - 50

    def food_eaten(self):
        self.goto(
            randint((self.screen_width // 2) * -1, self.screen_width // 2),
            randint((self.screen_height // 2) * -1, self.screen_height // 2))
