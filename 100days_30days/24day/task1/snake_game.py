from turtle import *
from time import sleep
import snake
import food
import scoreboard

snake_segments = []
speed = 0.1


def default_settings():
    # screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    my_snake.create_def_snake()

    # Buttons
    snake.listen()
    screen.onkey(my_snake.head_up, "Up")
    screen.onkey(my_snake.head_down, "Down")
    screen.onkey(my_snake.head_left, "Left")
    screen.onkey(my_snake.head_right, "Right")


# def game_over():
#     game_over_text = turtle.Turtle()
#     game_over_text.hideturtle()
#     game_over_text.penup()
#     game_over_text.color("red")
#     game_over_text.write("GAME OVER!", align=scoreboard.ALIGEMENT,
#                          font=scoreboard.FONT)
#

def round_over():
    my_snake.reset_to_default()
    sboard.check_highest_score()


if __name__ == "__main__":

    # Inizitalization
    screen = Screen()
    screen.setup(600, 600)
    screen.screensize(600, 600)
    my_snake = snake.Snake(screen.screensize()[0], screen.screensize()[1])
    sboard = scoreboard.Scoreboard(screen.screensize()[1])

    apple = food.Food(screen.screensize()[0], screen.screensize()[1])
    default_settings()

    # Game
    game_is_on = True
    while game_is_on:
        screen.update()
        speed = 0.1
        sleep(speed)
        my_snake.move_snake()

        # Checking if apple is being eaten
        if my_snake.head.distance(apple) <= 15:
            my_snake.add_segment(my_snake.snake_segments[-1].position())
            apple.food_eaten()

            if (speed - 0.1 - 0.02 * sboard.score) > 0:
                speed - 0.1 - 0.02 * sboard.score
                sleep(speed)
            sboard.update_score(1)

        # Checking collision with wall
        if my_snake.check_collision_wall() or my_snake.check_collision_tail():
            round_over()

    screen.exitonclick()
