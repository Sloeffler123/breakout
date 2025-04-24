from turtle import Turtle
class PlayerBlock(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('lightblue')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed(0)
        self.goto(0, -310)
        self.lives = 3
    def move_right(self):
        if self.check_boundry_right() != True:
            self.setheading(0)
            self.forward(7)
    def move_left(self):
        if self.check_boundry_left() != True:
            self.setheading(180)
            self.forward(7)
    def check_boundry_left(self):
        location_x = self.xcor()
        if location_x <= -340: 
            return True  
        return False    
    def check_boundry_right(self):
        location_x = self.xcor()
        if location_x >= 340:
            return True     
        return False   
    
