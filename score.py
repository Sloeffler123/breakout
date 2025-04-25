from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('grey')
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.score = 0
        self.time = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 400)
        self.write(arg=f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))
        self.score += 10

                