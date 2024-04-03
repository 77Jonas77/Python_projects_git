"""Pong Game"""
from time import sleep
from turtle import *
import paddle
import ball
import scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

if __name__ == "__main__":
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    paddle_1 = paddle.Paddle(1)
    paddle_2 = paddle.Paddle(2)
    scboard_1 = scoreboard.Scoreboard(SCREEN_WIDTH / 2, 1)
    scboard_2 = scoreboard.Scoreboard(SCREEN_WIDTH / 2, 2)
    game_ball = ball.Ball()

    screen.listen()
    screen.onkey(paddle_1.move_up, 'w')
    screen.onkey(paddle_2.move_up, 'Up')
    screen.onkey(paddle_1.move_down, 's')
    screen.onkey(paddle_2.move_down, 'Down')
    screen.update()

    game_on = True
    while game_on:
        game_ball.move_ball()
        sleep(0.05)

        # bouncing wall
        if game_ball.ycor() >= SCREEN_HEIGHT // 2 \
                or game_ball.ycor() <= -(SCREEN_HEIGHT // 2):
            game_ball.bounce_y()

        # bounce paddle1
        if game_ball.distance(
                paddle_1) <= 50 and game_ball.xcor() <= paddle_1.xcor():
            game_ball.bounce_x()
        elif game_ball.distance(
                paddle_2) <= 50 and game_ball.xcor() >= paddle_2.xcor():
            game_ball.bounce_x()
        else:
            # players miss hitting the ball
            if game_ball.distance(
                    paddle_1) > 50 and game_ball.xcor() <= paddle_1.xcor():
                scboard_2.update_score(1)
                game_ball.goto(0, 0)
                game_ball.bounce_x()
            elif game_ball.distance(
                    paddle_2) > 50 and game_ball.xcor() >= paddle_2.xcor():
                scboard_1.update_score(1)
                game_ball.goto(0, 0)
                game_ball.bounce_x()
        screen.update()

    screen.exitonclick()
