from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game by Required")
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.refresh()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 40 and ball. xcor() > 350 or ball.distance(l_paddle) < 40 and ball.xcor() < -355:
        ball.bounce_x()

    # Reset game when ball didn't hit the paddle of the right player
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_points()

    # Reset game if ball didn't hit the paddle of the left player
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_points()


screen.exitonclick()
