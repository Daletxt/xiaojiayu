print("Hello world")
temp = input("猜一下小甲鱼现在心里\
想的是哪个数字:\n""(你有5次机会)\n")
guess = int(temp)
if guess == 8:
	print("卧槽，你是小甲鱼心里蛔虫吗？！")
	print("哼，猜中了也没有奖励！")
else:
	i = 0
	while guess != 8:
		i += 1
		if guess != 8:
			if guess > 8:
				print("哥，大了大了~~\n你还有",(5-i),"次机会。\n")
			else:
				print("嘿，小了小了~~\n你还有",(5-i),"次机会。\n")
			temp = input("请重新输入吧：\n")
			guess = int(temp)
		if i > 3:
			if guess == 8:
				print("卧槽，你是小甲鱼心里蛔虫吗？！")
				print("哼，猜中了也没有奖励！")
			else:
				if guess > 8:
					print("哥，大了大了~~\n你没有机会啦！")
				else:
					print("嘿，小了小了~~\n你没有机会啦！")
				print("小甲鱼心里想的是8。")
			break
	else:
		print("卧槽，你是小甲鱼心里蛔虫吗？！")
		print("哼，猜中了也没有奖励！")
print("游戏结束，不玩啦~")









































