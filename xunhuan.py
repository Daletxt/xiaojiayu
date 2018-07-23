
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
	print('A')
if 90 > score >= 80:
	print('B')
if 80 > score >= 60:
	print('C')
if 60 > score >= 0:
	print('D')
if score < 0 or score > 100:
	print('输入错误！')

	

score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
	print('A')
else:
	if 90 > score >= 80:
		print('B')
	else:
		if 80 > score >= 60:
			print('C')
		else:
			if 60 > score >= 0:
				print('D')
			else:
				if score < 0 or score > 100:
					print('输入错误！')

					

score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
	print('A')
elif 90 > score >= 80:
	print('B')
elif 80 > score >= 60:
	print('C')
elif 60 > score >= 0:
	print('D')
elif score < 0 or score > 100:
	print('输入错误！')



score = int(input('请输入一个分数：'))
assert 0 <= score <=100
if 100 >= score >= 90:
	print('A')
elif 90 > score >= 80:
	print('B')
elif 80 > score >= 60:
	print('C')
elif 60 > score >= 0:
	print('D')
'''

'''
member=['你好','22','333','4444','55555']
for each in member:
	print(each,len(each))
for i in range(1,10,2):
#参数：range(起始（包含）,终止（不包含）,步进):参数可选1,2,3个
#一参数：起始默认0，步进1。 两参数，步进默认1。
	print(i)


bingo = '你是帅哥'
answer = input("请输入小甲鱼最想听的一句话：")
while True:
	if answer == bingo:
		break
	answer = input('抱歉，错了，请重新输入(答案正确才能退出游戏)：\n')

print('哎哟，帅哦~')
print('您真是小甲鱼肚子里的蛔虫啊^_^')



#continue:终止本轮循环并开始下一轮循环(循环条件为True时，否则退出循环)。
for i in range(10):
	if i%2 != 0:
		print(i)
		continue
	i += 2
	print(i)










