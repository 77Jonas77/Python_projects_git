import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def play_game():
    screen.listen()
    screen.onkey(pl.move_forward, "space")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        carmng.move_cars()
        screen.update()

        # Checking if turtle goes to next lvl
        if pl.check_is_nextlvl():
            scboard.increase_level()
            carmng.increase_diff_level()
            pl.move_to_starting_position()

        # Checking if turtle collisioned with car (game over)
        for car in carmng.cars:
            if pl.distance(car) < 20:
                scboard.game_over()
                game_is_on = False
                break


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    pl = Player()
    scboard = Scoreboard()
    carmng = CarManager()

    play_game()
    screen.exitonclick()
    # without play_again func
