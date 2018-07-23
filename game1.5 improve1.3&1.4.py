print("Hello world!")
import random
print("##########    猜数字小游戏    ###########")
print("# 1.密码“开虐”开始游戏 2.任意键退出游戏 #")
print("#     注：猜错3次游戏自动退出.          #")
print("#########################################")
put = input("请输入密码：")
if put == "开虐":
	i = 3
	secret = random.randint(1,10)
	while i > 0:
		temp = input("猜一下小甲鱼现在心里想的是数字几：")
		temp2 = temp.strip()
		if temp2.isdigit():
			guess = int(temp2)
			if guess == secret:
				exit("是%d，卧槽，你是小甲鱼心里蛔虫吗？！\
				哼，猜中了也没有奖励！游戏结束")
			elif guess > secret:
				print("哥，大了大了~~\n你还有",i-1,"次机会。")
			elif i == 1:
				exit("嘿，你没有机会啦！\n小甲鱼心里想的是",secret)
			else:
				print("嘿，%d小了小了~~\n你还有%d次机会。" % (guess,i-1))		
		else:
			print("你输入的：'%s'不是一个数字，请输入一个整数" % temp)
			i -= 1
		i -= 1
else:
	exit("游戏结束，不玩啦~")







































