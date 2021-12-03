import random
import string
s = ""
print(0x5)
print(0x14)
for _变量_ in range(random.randint(0x5, 0x14)):
    c = random.choice(string.ascii_lowercase)
    s = s + c
sl = list(s)
while True:
    print("现在的字符串是：{}".format(sl))
    p = input("请选择你要拿走的字符")
    if p in sl:
        id = sl.index(p)
        sl.pop(id)
        print('你选择拿走的字符是：{}'.format(sl))
        print('你抽取后{}'.format(sl))
    else:
        print("你选择的字符不存在，请重新选择")
        continue
    oc = 0
    cc = []
    for j in sl:
        if j not in cc:
            cc.append(j)
            n = sl.count(j)
            if n % 2 == 1:
                oc += 1
    if oc <= 1:
        print('你赢了')
        break

    oc = 0
    print("现在的字符串是：{}".format(sl))
    com = random.choice(sl)
    id = sl.index(com)
    sl.pop(id)
    print('电脑选择拿走的字符是：{}'.format(sl))
    print('电脑抽取后{}'.format(sl))
    oc = 0
    cc = []
    for j in sl:
        if j not in cc:
            cc.append(j)
            n = sl.count(j)
            if n % 2 == 1:
                oc += 1
    if oc <= 1:
        print('你赢了')
        break
