import turtle as t
import random
tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)

    color_tupple= (r,g,b)
    return color_tupple
colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0,90,180,270]



tim.speed("fastest")
tim.pensize(10)

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
