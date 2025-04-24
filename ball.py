from turtle import Turtle

class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.color('white')
        self.ball.shape('circle')
        self.ball.penup()
        self.ball.speed(0)
        self.ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.ball.goto(0,-290)
    def ball_movement(self):
        speed = 2
        print(self.ball.ycor())
        print(self.ball.xcor())
        self.ball.sety(self.ball.ycor() + speed)
        location = self.ball.ycor()
        if location >= 480:
            speed *= -1
        
        
    