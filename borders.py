from turtle import Turtle

class Border(Turtle):
    def __init__(self, x, y, size_1, size_2):
        super().__init__()
        self.x = x
        self.y = y
        self.shape('square')
        self.shapesize(size_1, size_2)
        self.penup()
        self.color('grey')
        self.speed(0)
        self.goto(x, y)