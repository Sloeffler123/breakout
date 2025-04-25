from turtle import Screen
from player import PlayerBlock
from ball import Ball
from blocks import generate_blocks
from borders import Border
from score import Score
from lives import PlayerLives
import time

screen = Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes('-fullscreen', True)
screen.bgcolor('black')
screen.tracer(0)
time.sleep(1)

player = PlayerBlock()
player_lives = PlayerLives()
ball = Ball()
score = Score()
player_lives.display_lives()
border_left = Border(-393, 0, 50, 1)
border_right = Border(393, 0, 50, 1)
border_top = Border(0, 370, 1, 40)

screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_left, key='a')

blocks_list = generate_blocks()

screen.listen()
#Main loop
on = True
count = 0
while on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement()
    ball.collision_wall()
    if ball.distance(player) < 60:
        ball.paddle_collision()
    if ball.ycor() <= -485:
        player_lives.lives -=  1
        if player_lives.lives == 0:
            ball.clear()
            on = False
        player_lives.display_lives()
        ball.ball_reset()
            
    for block in blocks_list:
        if ball.distance(block) < 30:
            count += 1
            if count == 5:
                ball.block_collision()
                count = 0
            score.update_score()
            blocks_list.remove(block)
            block.hideturtle()
            ball.paddle_collision()   
        if len(blocks_list) == 0:
            score.winner()
            on = False    

screen.exitonclick()