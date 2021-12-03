import turtle
import random
b = turtle.Pen()
b.hideturtle()
a = turtle.Screen()
p = 0
c = 0
for i in range(10):
    player = int(a.textinput("剪刀1-石头2-布3", "请输入拳名对应的数字："))
    computer = random.randint(1, 3)
    if player == 1:
        print("玩家出了：剪刀")
    elif player == 2:
        print("玩家出了：石头")
    elif player == 3:
        print("玩家出了：布")
    if computer == 1:
        print("电脑出了：剪刀")
    elif computer == 2:
        print("电脑出了：石头")
    elif computer == 3:
        print("电脑出了：布")
    print("---------------------------")
    if player == computer:
        print("平局")
        b.pencolor("gray")
        b.dot(20)
    elif player == 1 and computer == 2:
        print("电脑胜利")
        b.pencolor("red3")
        b.dot(20)
        c = c + 1
    elif player == 1 and computer == 3:
        print("玩家胜利")
        b.pencolor("darkgreen")
        b.dot(20)
        p = p + 1
    elif player == 2 and computer == 1:
        print("玩家胜利")
        b.pencolor("darkgreen")
        b.dot(20)
        p = p + 1
    elif player == 2 and computer == 3:
        print("电脑胜利")
        b.pencolor("red3")
        b.dot(20)
        c = c + 1
    elif player == 3 and computer == 2:
        print("玩家胜利")
        b.pencolor("darkgreen")
        b.dot(20)
        p = p + 1
    elif player == 3 and computer == 1:
        print("电脑胜利")
        b.pencolor("red3")
        b.dot(20)
        c = c + 1
    b.penup()
    b.forward(25)
    b.pendown()
print("玩家胜利",p,"局")
print("电脑胜利",c,"局")
print("平局",10 - p - c, "局")
turtle.done()
