import turtle
import random
a = turtle.Pen()
a.hideturtle()
a.speed(0)
b = turtle.Screen()
b.bgcolor('midnightblue')
a.penup()
a.goto(-200,200)
a.pendown()
a.pencolor('lightyellow')
a.dot(100)
a.forward(30)
a.pencolor('midnightblue')
a.dot(100)
v = [[0,0],[-90,20],[-200,-25],[100,-20],[150,-110],[240,-90],[250,30]]
def s(size):
    a.fillcolor('gold')
    a.begin_fill()
    t = 0
    for j in range(5):
        a.forward(size)
        a.left(72)
        a.forward(size)
        a.right(144)
    a.end_fill()
size = [20, 11, 14, 7, 6, 11, 17]
for x in range(7):
    a.penup()
    a.goto(v[x])
    a.pendown()
    a.pencolor('gold')
    s(size[x])

turtle.done()
