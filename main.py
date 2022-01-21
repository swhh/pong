from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BG_COLOR = 'black'
NET_SIZE = 10
PEN_THICK = 5
R_POSITION = (350, 0)
L_POSITION = (-350, 0)

screen = Screen()
screen.bgcolor(BG_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)
divide = Turtle()
divide.hideturtle()
divide.pencolor('white')
divide.shape('square')
divide.pensize(PEN_THICK)
divide.pu()
divide.goto((0, SCREEN_HEIGHT))
divide.seth(270)

while divide.ycor() > -(SCREEN_HEIGHT / 2):
    divide.forward(NET_SIZE)
    if divide.isdown():
        divide.pu()
    else:
        divide.pd()
r_paddle = Paddle(R_POSITION)
l_paddle = Paddle(L_POSITION)
ball = Ball()
scoreboard = ScoreBoard()
screen.update()
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')


game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if abs(ball.ycor()) > (SCREEN_HEIGHT / 2) - 10:
        ball.bounce(True)

    if (ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50) and abs(ball.xcor()) > (SCREEN_WIDTH / 2) - 80:
        ball.bounce(False)

    if abs(ball.xcor()) > (SCREEN_WIDTH / 2) - 20:
        if max(0.0, ball.xcor()):
            scoreboard.update_score(0)
        else:
            scoreboard.update_score(1)

        ball.reset_position()

screen.exitonclick()