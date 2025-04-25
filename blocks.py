from turtle import Turtle

class Blocks(Turtle):
    def __init__(self, color, x, y, id):
        super().__init__()
        self.id = id
        self.y = y
        self.x = x
        self.color(color)
        self.penup()
        self.shape('square')
        self.shapesize(1, 3)
        self.speed(1)
        self.goto(self.x, self.y)

def generate_blocks():
    blocks_lst = []

    x = -420
    for i in range(1, 12):
        x += 70
        block = Blocks('red', x, 260, i)
        blocks_lst.append(block)

    x = -420   
    for i in range(12, 23):
        x += 70
        block = Blocks('red', x, 230, i)
        blocks_lst.append(block)

    x = -420 
    for i in range(23, 34):
        x += 70
        block = Blocks('orange', x, 200, i)
        blocks_lst.append(block)

    x = -420    
    for i in range(34, 45):
        x += 70
        block = Blocks('orange', x, 170, i)
        blocks_lst.append(block)

    x = -420    
    for i in range(45, 56):
        x += 70
        block = Blocks('yellow', x, 140, i)
        blocks_lst.append(block)

    x = -420    
    for i in range(56, 67):
        x += 70
        block = Blocks('yellow', x, 110, i)
        blocks_lst.append(block)

    x = -420    
    for i in range(67, 78):
        x += 70
        block = Blocks('green', x, 80, i)
        blocks_lst.append(block)

    x = -420    
    for i in range(78, 89):
        x += 70
        block = Blocks('green', x, 50, i)
        blocks_lst.append(block)

    return blocks_lst
