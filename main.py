from turtle import Screen, Turtle
from player import PlayerBlock
from ball import Ball
import time
screen = Screen()
screen.setup(800, 1000)
screen.bgcolor('black')
screen.tracer(0)
class RectObjects:
    def __init__(self):
        pass

class Score:
    def __init__(self):
        pass

time.sleep(1)
player = PlayerBlock()
ball = Ball()
screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_left, key='a')
screen.onkeyrelease(fun=player.move_right, key='d')
screen.onkeyrelease(fun=player.move_left, key='a')
screen.listen()
#Main loop
on = True
while on:
    time.sleep(0.01)
    screen.update()
    ball.ball_movement()
    ball.collision_wall()
    if ball.distance(player) < 50:
        ball.paddle_collision()
    if ball.ycor() <= 485:
        ball.reset()
        player.lives -= 1    
    
screen.exitonclick()
    
