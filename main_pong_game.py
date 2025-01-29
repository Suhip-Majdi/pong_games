import turtle
from paddle_pong import Paddle
from ball_pong import Ball
from pong_scorebord import Scoreboard
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_padlle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 380:
        score.increase_score_l()
        ball.reset_position()

    # Detect Left paddle misses
    if ball.xcor() < -380:
        score.increase_score_r()
        ball.reset_position()

screen.exitonclick()
