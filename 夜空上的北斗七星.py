import turtle

mypen = turtle.Pen()
mypen.hideturtle()
mypen.speed(0)
myscreen = turtle.Screen()
myscreen.bgcolor("midnightblue")

#画笔移动
mypen.penup()
mypen.goto(-200, 200)
mypen.pendown()

#画月亮
mypen.pencolor("lightyellow")
mypen.dot(100)
mypen.forward(30)
mypen.pencolor("midnightblue")
mypen.dot(100)

#定义画星星的函数


def star(size):
    mypen.pencolor("gold")
    mypen.begin_fill()
    mypen.fillcolor("gold")
    for i in range(5):
        mypen.forward(size)
        mypen.left(72)
        mypen.forward(size)
        mypen.right(144)
    mypen.end_fill()


#存储星星坐标和大小
pos_list = [[0, 0], [-90, 20], [-200, -25], [100, -20],
            [150, -110], [240, -90], [250, 30]]
size_list = [20, 11, 14, 5, 8, 11, 17]

#for循环遍历列表
for i in range(7):
    mypen.penup()
    mypen.goto(pos_list[i])
    mypen.pendown()
    star(size_list[i])

turtle.done()
