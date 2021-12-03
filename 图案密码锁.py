import turtle
a = turtle.Pen()
b = turtle.Screen()
a.hideturtle()
a.speed(0)
pos = [[-100,100],[0,100],[100,100],[-100,0],[0,0],[100,0],[-100,-100],[0,-100],[100,-100]]
a.pencolor('light sky blue')
for i in pos:
	a.penup()
	a.goto(i)
	a.pendown()
	a.dot(40)
ans = [1,3,5,6,8,9,2,4,7]
a.color('deep sky blue')
a.pensize(3)
a.penup()
f = True
for i in ans:
    num = int(b.textinput('输入','请输入一个数字'))
    if num != i:
        f = False
    cho = pos[num - 1]
    a.goto(cho)
    a.pendown()
    a.dot(20)
if f:
    print('解锁成功')
else:
    print('解锁失败')
turtle.done()