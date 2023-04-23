from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.score=0
        self.write(f"Score={self.score}",move=False,font=FONT)
    def increment(self):
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.score+=1
        self.write(f"Score={self.score}", move=False, font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",move=True,font=FONT)


