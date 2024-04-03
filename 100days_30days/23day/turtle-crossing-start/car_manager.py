import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
BASE_OBSTACLE_AMOUNT = 20
OBSTACLE_INCREMENT = 5


def create_car():
    """Creating 1 obstacle (car)"""
    new_car = Turtle(shape="square")
    new_car.color(random.choice(COLORS))
    new_car.penup()
    new_car.shapesize(1, 2)
    new_car.goto(random.randint(-300, 300), random.randint(-250, 250))
    return new_car


class CarManager:
    """Managing obstacles (cars) class """

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

        # Creating set of cars / obstactles
        for _ in range(BASE_OBSTACLE_AMOUNT):
            self.cars.append(create_car())

    def move_cars(self):
        """Moving all cars and managing whether is out of screen"""
        for car in self.cars:
            if car.xcor() > 300:
                car.goto(-300, random.randint(-250, 250))
            else:
                car.goto(car.xcor() + self.speed, car.ycor())

    def increase_speed(self):
        """Increase speed of obstacles"""
        self.speed += MOVE_INCREMENT

    def increase_diff_level(self):
        """Increase level of gameplay"""
        # adding more obstacles
        for _ in range(OBSTACLE_INCREMENT):
            self.cars.append(create_car())

        # increasing speed of obstalces
        self.speed += MOVE_INCREMENT

    def reset_mng_to_default(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

        # Creating set of cars / obstactles
        for _ in range(BASE_OBSTACLE_AMOUNT):
            self.cars.append(create_car())
