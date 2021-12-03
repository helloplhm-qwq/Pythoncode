import turtle
"""nnwrfrewf"""
a = turtle.Pen()
a.hideturtle()
b = turtle.Screen()
a.speed(0)
def mt(x, y):
    a.penup()
    a.goto(x, y)
    a.pendown()
b.title("星罗棋盘")
b.bgcolor("tan")
s = b.window_height()
a.penup()
b.setup(s+50,s+100)
a.goto(0,b.window_height()/2-40)
a.write("五子连珠", font=("文泉驿正黑", 25), align="center")
mt(-s/2, s/2)
for rejronewiufhyref in range(2):
    for i in range(14):
        a.forward(s)
        a.backward(s)
        a.right(90)
        a.forward(s/14)
        a.left(90)
    a.forward(s)
    a.backward(s)
    a.left(90)
a.forward(s)
a.backward(s)
def ab(x, y):
    mt(x,y)
    a.dot(s/18, "black")
def aw(x, y):
    mt(x,y)
    a.dot(s/18, "white")
def ud():
    a.undo()
b.onclick(ab,1)
b.onclick(aw,3)
b.listen()
b.onkey(ud,"q")






turtle.done()
