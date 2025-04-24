from turtle import Screen, Turtle
from player import PlayerBlock
from ball import Ball
import time
screen = Screen()
screen.setup(800, 1000)
screen.bgcolor('black')

 
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
screen.listen()
#Main loop
for i in range(400):
    ball.ball_movement()
screen.exitonclick()
    
