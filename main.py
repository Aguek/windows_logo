import turtle
from turtle import *

turtle.setup(width=500, height=500)
speed("slowest")
bgcolor('black')
penup()
goto(-100, 100)
pendown()
color('skyblue')
begin_fill()
goto(100, 100)
goto(100, -100)
goto(-100, -100)
goto(-100, 60)
end_fill()

penup()

goto(0, 100)
pendown()
color("black")
pensize(5)
goto(0, -100)

penup()
goto(100, 0)
pendown()
goto(-100, 0)
Screen().exitonclick()
# map = Turtle()
# screen = Screen()
# map.setheading(145)
# map.penup()
# map.forward(250)
# map.setheading(-45)
# map.pendown()
#
#
# def forward(steps):
#     map.forward(10 * steps)
#
# def left(degrees):
#     map.left(degrees)
#
# def right(degrees):
#     map.right(degrees)
#
#
# for points in range(1):
#     forward(3)
#     left(60)
#     forward(1)
#     right(10)
#     forward(2.5)
#     right(60)
#     forward(2)
#     left(50)
#     forward(3)
#     left(80)
#     forward(2)
#     right(20)
#
# # screen.listen()
# # screen.onkey(key="r", fun=right)
# # screen.onkey(key="l", fun=left)
# # screen.onkey(key="g", fun=forward)
# screen.exitonclick()
