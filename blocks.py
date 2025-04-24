from turtle import Turtle

class Blocks(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.y = y
        self.x = x
        self.color(color)
        self.penup()
        self.shape('square')
        self.shapesize(1, 3)
        self.speed(1)
        self.goto(self.x, self.y)

#need to make an id for each block object made and store every obect in one list. so when the ball hits a block i iterate over reversed list looking for the id and deleting that block
def red_blocks():
    red_block_lst = []
    x = -420
    for i in range(11):
        x += 70
        block = Blocks('red', x, 260)
        red_block_lst.append(block)
    j = -420    
    for i in range(11):
        j += 70
        block = Blocks('red', j, 230)
        red_block_lst.append(block)
   
def orange_blocks():
    orange_blocks_lst = []  
    x = -420
    for i in range(11):
        x += 70
        block = Blocks('orange', x, 200)
        orange_blocks_lst.append(block)
    j = -420    
    for i in range(11):
        j += 70
        block = Blocks('orange', j, 170)
        orange_blocks_lst.append(block)
       
def yellow_blocks():
    yellow_blocks_lst = [] 
    x = -420
    for i in range(11):
        x += 70
        block = Blocks('yellow', x, 140)
        yellow_blocks_lst.append(block)
    j = -420    
    for i in range(11):
        j += 70
        block = Blocks('yellow', j, 110)
        yellow_blocks_lst.append(block)
       
def green_blocks():
    green_blocks_lst = [] 
    x = -420
    for i in range(11):
        x += 70
        block = Blocks('green', x, 80)
        green_blocks_lst.append(block)
    j = -420    
    for i in range(11):
        j += 70
        block = Blocks('green', j, 50)
        green_blocks_lst.append(block)






