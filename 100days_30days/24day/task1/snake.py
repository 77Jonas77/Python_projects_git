"""Snake class"""
from turtle import *
from time import sleep

MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, screen_width, screen_height):
        self.head = None
        self.snake_segments = []
        self.screen_height = screen_height
        self.screen_width = screen_width

    def create_def_snake(self):
        """Initialize a snake"""
        for i in range(3):
            seg = Turtle("square")
            seg.color("pink")
            seg.penup()
            seg.goto((i * 20) * -1, 0)
            self.snake_segments.append(seg)
        self.head = self.snake_segments[0]

    def add_segment(self, posit):
        """Adding a segment to the snake"""
        seg = Turtle("square")
        seg.color("pink")
        seg.penup()
        seg.goto(posit)
        # seg.goto((i * 20) * -1, 0)
        self.snake_segments.append(seg)

    def move_snake(self):
        """Moving the snake"""
        for indx in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[indx].goto(
                self.snake_segments[indx - 1].xcor(),
                self.snake_segments[indx - 1].ycor())
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def head_up(self):
        """Setting the head uppowards"""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def head_down(self):
        """Setting the head uppowards"""
        if self.head.heading() != UP:
            self.head.setheading(270)

    def head_left(self):
        """Setting the head uppowards"""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def head_right(self):
        """Setting the head uppowards"""
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def check_collision_wall(self):
        """Checking if snake head collides with 'wall' """
        if (self.head.xcor() > self.screen_width // 2
                or self.head.xcor() < -self.screen_width // 2
                or self.head.ycor() > self.screen_height // 2
                or self.head.ycor() < -self.screen_height // 2):
            return True
        return False

    def check_collision_tail(self):
        for idx, tail in enumerate(self.snake_segments[1:]):
            if tail.distance(self.head) < 10:
                return True
        return False

    def reset_to_default(self):
        """Resetting snake settings to default"""
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_def_snake()
