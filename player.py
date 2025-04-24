from turtle import Turtle
class PlayerBlock:
    def __init__(self):
        self.player = Turtle()
        self.player.penup()
        self.player.color('lightblue')
        self.player.shape('square')
        self.player.shapesize(stretch_wid=1, stretch_len=5)
        self.player.speed(0)
        self.player.goto(0, -310)
    def move_right(self):
        if self.check_boundry_right() != True:
            self.player.setheading(0)
            self.player.forward(15)
    def move_left(self):
        if self.check_boundry_left() != True:
            self.player.setheading(180)
            self.player.forward(15)
    def check_boundry_left(self):
        location_x = self.player.xcor()
        if location_x <= -340: 
            return True  
        return False    
    def check_boundry_right(self):
        location_x = self.player.xcor()
        if location_x >= 340:
            return True     
        return False   
    