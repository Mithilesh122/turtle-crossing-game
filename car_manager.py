from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "blue", "purple","green"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self,shap):
        super(CarManager, self).__init__()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.shape(shap)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(280,random.randint(-250,250))
        self.setheading(180)
    def move(self,spedv,tim):
        self.forward(5*spedv)
        time.sleep(0.1*tim)














