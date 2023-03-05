import turtle
from turtle import *

bgcolor("black")
pensize(3)
speed(0)

color('white', 'yellow')
begin_fill()
while True:
    forward(300)
    left(250)
    if abs(pos()) < 1:
        break

# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     color(colours)
#     circle(150)
#     left(60)

# for i in range(10):
#     for colours in ["red", "orange", "yellow", "green", "blue", "purple", "white"]:
#         turtle.color(colours)
#         turtle.circle(150)
#         # turtle.left(10)
#         right(6)

end_fill()
done()