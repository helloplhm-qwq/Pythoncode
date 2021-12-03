import turtle
import random
mypen = turtle.Pen()
mypen.hideturtle()
mypen.speed(0)
myscreen = turtle.Screen()
myscreen.bgcolor("midnightblue")

#画笔移动
def m(x,y):
    mypen.penup()
    mypen.goto(x, y)
    mypen.pendown()


m(-200, 200)
myscreen.tracer(0)

#画月亮
mypen.pencolor("lightyellow")
mypen.dot(100)
mypen.forward(30)
mypen.pencolor("midnightblue")
mypen.dot(100)

#定义画星星的函数


def star(size,color):
    mypen.pencolor(color)
    mypen.begin_fill()
    mypen.fillcolor(color)
    for i in range(5):
        mypen.forward(size)
        mypen.left(72)
        mypen.forward(size)
        mypen.right(144)
    mypen.end_fill()

def rs():
    s = random.choice([4, 6, 8])
    c = random.choice(['gold', 'yellow', 'orange', 'violet'])
    return s,c


def ds(x,y):
    s, c = rs()
    m(x,y)
    star(s,c)


myscreen.onclick(ds,btn=1)


def dd(x,y):
    s,c = rs()
    m(x,y)
    mypen.pencolor(c)
    mypen.dot(s)
myscreen.onclick(dd,btn=3)

turtle.done()
