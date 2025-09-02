from turtle import Turtle,Screen
from snakee import Snakee
import time

screen= Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snakee=Snakee()

screen.listen()
screen.onkey(snakee.up,"Up")
screen.onkey(snakee.down,"Down")
screen.onkey(snakee.left,"Left")
screen.onkey(snakee.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.3)

    snakee.move()

    

    

    













screen.exitonclick()