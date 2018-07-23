print('hello,world')
#while else
def showMaxFactor(num):
	count = num // 2
	while count > 1:
		if num % count ==0:
			print('%d最大的约数(除了它本身)是%d' % (num,count))
			break
		count -= 1
	else:
		print('%d是素数！' % num)
		
num = int(input('请输入一个数：'))
showMaxFactor(num)

#if else

#else
try:
	print(int('123'))
except ValueError as reason:
	print('出错啦：' + str(reason))
else:
	print('没有任何异常！')



import os
os.chdir('D:/Python/xiaojiayu')
	
try:
	f = open('data.txt','w')#用with：with open('data.txt','w') as f:下边缩进
	for each_line in f:
		print(each_line)
except OSError as reason:
	print('出错啦：' + str(reason))
finally:
	f.close()





























































































