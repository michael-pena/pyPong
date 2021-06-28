from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

scoreboard = ScoreBoard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=l_paddle.go_up)
screen.onkey(key="Down", fun=l_paddle.go_down)

screen.onkey(key="w", fun=r_paddle.go_up)
screen.onkey(key="s", fun=r_paddle.go_down)

game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bounce off upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce of the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # if ball goes out of bounds award point to other player (left) and reset ball
    if ball.xcor() > 420 or ball.xcor() < -420:
        if ball.xcor() > 420:
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            print(f"+1 point to the left player. Total: {scoreboard.l_score}")
        else:
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            print(f"+1 point to the right player. Total: {scoreboard.r_score}")

        ball.reset()

screen.exitonclick()
