from turtle import Turtle

class PlayerLives(Turtle):
    def __init__(self):
        super().__init__()
        self.color('grey')
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.lives = 3

    def display_lives(self):
        self.clear()
        self.goto(0, 490)
        if self.lives != 0:
            self.write(arg=f'Lives: {self.lives}', align='center', font=('Courier', 20, 'normal'))
        else:
            self.write(arg='GAME OVER', align='Center', font=('Courier', 20, 'normal'))