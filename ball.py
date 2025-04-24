from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        ran_num = random.randint(0, 150)
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(0,-250)
        self.setheading(ran_num)
        self.speed = 2
        self.x = 2
        self.y = 2
    def ball_movement(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def collision_wall(self):    
        location_y = self.ycor()
        location_x = self.xcor()
        if location_x >= 385 or location_x <= -385:
            self.x *= -1
        if location_y >= 485:
            self.y *= -1
    def paddle_collision(self):
        self.y *= -1 

    def ball_reset(self):
        self.reset()
        self.penup()  
        self.color('white')
        self.shapesize(0.5, 0.5)
        self.goto(0, -250)
        self.speed = 2
        self.setheading(90)
          

        
    