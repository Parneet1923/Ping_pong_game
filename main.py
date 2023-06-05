from turtle import Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from center_line import CenterLine

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()

center_line = CenterLine()
center_line.draw_line()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_on = True
speed = 0.1
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(r_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_off_pedal()
        speed *= 0.9

    if ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_off_pedal()
        speed *= 0.9

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.player1_inc_score()
        speed = 0.25

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.player2_inc_score()
        speed = 0.25

    if scoreboard.check_winner():
        game_on = False

screen.exitonclick()
