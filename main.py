from turtle import Screen, Turtle
from player import PlayerBlock
from ball import Ball
from blocks import red_blocks, orange_blocks, yellow_blocks, green_blocks
from borders import Border
from score import Score
import time

screen = Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes('-fullscreen', True)
screen.bgcolor('black')
screen.tracer(0)
time.sleep(1)

player = PlayerBlock()
ball = Ball()
score = Score()
border_left = Border(-393, 0, 50, 1)
border_right = Border(393, 0, 50, 1)
border_top = Border(0, 370, 1, 40)

screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_left, key='a')
screen.onkeyrelease(fun=player.move_right, key='d')
screen.onkeyrelease(fun=player.move_left, key='a')

red_blocks()
orange_blocks()
yellow_blocks()
green_blocks()

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
    if ball.ycor() <= -485:
        player.lives -= 1    
        ball.ball_reset()
    
screen.exitonclick()
    
