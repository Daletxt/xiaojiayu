#递归，求阶乘1*2*3*4*5
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number,result))

#斐波那契数列
#1,2,3,4,5,6,7, 8, 9, 10,11,12, 13, 14, 15
#1,1,2,3,5,8,13,21,34,55,89,144,233,377,610

def F(n):
	n1 = 1
	n2 = 1
	
	if n < 1:
		print('输入有误！')
		return -1
	while (n-2) > 0:
		n3 = n2 + n1
		n1 = n2
		n2 = n3
		n -= 1
	return  n3

result = F(8)
if result != -1:
	print('总共有%e对小兔崽子诞生！' % result)
#递归求斐波那契数列
def fa(n):
	if n < 1:
		print('输入有误！')
		return -1
	if n == 1 or n ==2:
		return 1
	else:
		return fa(n-1) + fa (n-2)

result = fa(8)
if result != -1
	print('总共有%e对小兔崽子诞生！' % result)


























































































