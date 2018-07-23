import random
secret = random.randint(1,100)
temp = input("猜一下小甲鱼现在心里\
想的是哪个数字:\n""(你有6次机会)\n")
guess = int(temp)
if guess == secret:
	print("卧槽，你是小甲鱼心里蛔虫吗？！")
	print("哼，猜中了也没有奖励！")
else:
	i = 0
	while guess != secret:
		i += 1		
		if guess > secret:
			print("哥，大了大了~~\n你还有",(6-i),"次机会。\n")
		else:
			print("嘿，小了小了~~\n你还有",(6-i),"次机会。\n")
		temp = input("请重新输入吧：\n")
		guess = int(temp)
		if i == 5:
			if guess == secret:
				print("卧槽，你是小甲鱼心里蛔虫吗？！")
				print("哼，猜中了也没有奖励！")
			else:
				print("嘿，你没有机会啦！\n小甲鱼心里想的是",secret)
			break
	else:
		print("卧槽，你是小甲鱼心里蛔虫吗？！")
		print("哼，猜中了也没有奖励！")			
print("游戏结束，不玩啦~")









































