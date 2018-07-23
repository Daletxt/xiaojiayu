print("Hello world")
temp = input("猜一下小甲鱼现在心里想的是哪个数字:\n")
guess = int(temp)
if guess == 8:
	print("卧槽，你是小甲鱼心里蛆虫吗？！")
	print("哼，猜中了也没有奖励！")
else:
	while guess != 8:
		if guess != 8:			
			if guess > 8:
				print("哥，大了大了~~")
			else:
				print("嘿，小了小了")
			temp = input("请重新输入吧：\n")
			guess = int(temp)
	else:
		print("卧槽，你是小甲鱼心里蛆虫吗？！")
		print("哼，猜中了也没有奖励！")
print("游戏结束，不玩啦~")









































