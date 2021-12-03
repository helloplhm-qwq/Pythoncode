from datetime import date,timedelta
import os
os.system("cmd.exe /c cls")
os.system("cmd.exe /c del /f /q datelist.txt>nul")
def check(num):
	return str(num) == str(num)[::-1]
def choose():
	start_year = int(input('请输入计算起始年份：'))
	end_year = int(input('请输入计算结束年份：'))
	sd = date(start_year,1,1)
	ed = date(end_year,12,31)
	os.system("cmd.exe /c echo 从{}年至{}年的对称日列表>datelist.txt".format(start_year,end_year))
	return sd,ed
try:
	start_date,end_date=choose()
except ValueError:
	print('输入值超出范围或有误')
delta = timedelta(days=1)
count = 0
while start_date<=end_date:
	s = start_date.strftime("%Y%m%d")
	if check(num=s):
		datelist1 = list(s)
		datelist = []
		if len(datelist1) < 8:
		    for i in range(8 - len(datelist1)):
		        datelist.append(0)
		    for j in datelist1:
		        datelist.append(j)
		    #print(len(datelist),'sssss',datelist)
		else:
		    for j in datelist1:
		        datelist.append(j)
		formateddate = str(str(datelist[0])+str(datelist[1])+str(datelist[2])+str(datelist[3])+'年'+str(datelist[4])+str(datelist[5])+'月'+str(datelist[6])+str(datelist[7])+'日')
		print(formateddate)
		with open("datelist.txt","a") as datelist:
			datelist.write("\n"+str(formateddate))
		count = count + 1
	start_date += delta
if count == 0:
	with open('datelist.txt','a') as datelist:
		datelist.write('这里似乎什么也没有')
	print("您所填写的日期内乜有对称日~")
else:
	print("计算已经完成，一共有{}个对称日，列表已保存至当前目录".format(count))
