import turtle
import random
a = turtle.Pen()
a.hideturtle()
b = turtle.Screen()
#b.tracer(0)
c = ["red","deep sky blue","green3","purple","orange","pink"]
pos = {"A":[0,0],"S":[100,0],"D":[200,0]}
def d(l):
    a.penup()
    a.goto(pos[l])
    a.pendown()
    a.pencolor(random.choice(c))
    a.write(l,font=("宋体",50))

for i in pos:
    a.penup()
    a.goto(pos[i])
    a.pendown()
    a.write(i,font=("宋体",50))
def da():
    d("A")


def ds():
    d("S")
def dd():
    d("D")


turtle.listen()
turtle.onkey(da,"a")
turtle.onkey(da,"A")
turtle.onkey(ds,"s")
turtle.onkey(ds,"S")
turtle.onkey(dd,"d")
turtle.onkey(dd,"D")

turtle.done()
