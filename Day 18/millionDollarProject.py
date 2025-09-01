import colorgram
import turtle as t
import random

tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

colors = colorgram.extract('Day 18\image.jpg', 30)

rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color= (r,g,b)
    rgb_colors.append(new_color)


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

t.colormode(255)

for i in range(1,num_of_dots+1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)

    if i%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=t.Screen()
screen.exitonclick()