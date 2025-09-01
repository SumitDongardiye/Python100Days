from turtle import Turtle as t, Screen

timmy=t()   # Created a new turtle object

print(timmy)
timmy.shape("turtle")
timmy.color("blue")

for i in range(0,4):
    timmy.forward(100)
    timmy.right(90)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

