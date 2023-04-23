import time
import turtle
from scoreboard import Scoreboard
from turtle import Screen
from player import FINISH_LINE_Y
from player import Player
from turtle import Turtle
from car_manager import CarManager
import random
from car_manager import COLORS

screen = Screen()
screen.tracer(0)
score=Scoreboard()
player=Player()
car=[]
for i in range(10):
  car.append(CarManager("square"))
screen.setup(width=600, height=600)
turtle.listen()
turtle.onkey(player.move_up,"Up")
game_is_on = True
spedv=5
screen.update()
tim=1
while game_is_on:
    r_num = random.randint(0, len(car) - 1)
    for i in car:
        if(player.distance(i)<10 or player.distance(car[r_num])<10):
            game_is_on=False
            score.gameover()
    if(player.ycor()>FINISH_LINE_Y):
        player.refresh()
        tim*=0.5
        car[r_num].move(spedv,tim)
        screen.update()
        score.increment()
    car[r_num].move(spedv,tim)
    for i in car:
        if(player.distance(i)<10 or player.distance(car[r_num])<10):
            game_is_on=False
            score.gameover()
    if(car[r_num].xcor()<-280):
        car[r_num].color(random.choice(COLORS))
        car[r_num].goto(280,random.randint(-250,250))
    screen.update()







screen.exitonclick()