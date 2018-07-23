print("Hello world")
i = 0
while i < 5:
	try:
		temp = input("猜一下小甲鱼现在心里想的是哪个数字:\n(你还有%d次机会。)\n" % (5-i))
		guess = int(temp)
		if guess == 8 and i == 0:
			print("一次就猜中，你是小甲鱼心里蛔虫吗？！\n奖励你个么么哒")
		else:
			while guess != 8:
				i += 1
				if guess > 8:
					print("哥，大了大了~~\n(你还有",(5-i),"次机会。)\n")
				else:
					print("嘿，小了小了~~\n(你还有%d次机会。)\n" % (5-i))
				temp = input("请重新输入吧：\n")
				guess = int(temp)
				if i == 4:
					if guess == 8:
						print("终于猜对了，这么慢没有奖励了！")
					elif guess > 8:
						print("哥，大了大了~~\n你没有机会啦！\n小甲鱼心里想的是8。")
					elif guess < 8:
						print("嘿，小了小了~~\n你没有机会啦！\n小甲鱼心里想的是8。")	
					break
			else:
				if i == 4:
					print("终于猜对了，这么慢没有奖励了！")
				else:
					print("卧槽，你是小甲鱼心里蛔虫吗？！\n哼，猜中了也没有奖励！")
		print("游戏结束，不玩啦~")
		break
	except ValueError:
		i += 1
		if i ==5:
			print("非法输入，最后一次机会你还皮，不跟你玩了，再也不见！")
		else:
			print("非法输入，机会-1！")



































