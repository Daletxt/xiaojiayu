'''
函数(function):有返回值
过程(procedure)是简单、特殊并且没有返回值
'''
def hello():
	print("Hello World")
	
temp = hello()
temp
print(temp)
type(temp)


def back():
	return [1,'小甲鱼',3.14]

back()
print(back())

def back():
	return 1,'小甲鱼',3.14

back()
print(back())

print("*************************************************")

#局部变量(Local Variable) 全局变量(Global Variable)
def discounts(price,rate):
	final_price = price * rate
	old_price = 88
#此处的old_price是python的屏蔽(Shadowing)机制新建的和函数外全局变量的同名局部变量
#	print('这里试图打印全局变量old_price的值：',old_price)
	print('修改后(函数内)old_price的值是：',old_price)
	return final_price
#局部变量：price、rate、final_price


old_price = float(input('请输入原价：'))
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price,rate)
print('修改后(函数外，全局变量)old_price的值是：',old_price)
print('打折后价格是：',new_price)
print(discounts(100,0.5))
#全局变量：old_price、new_price、rate

print("*************************************************")

#若一意孤行一定要在函数内部修改全局变量，使用global关键字
count = 5
def Myfun():
	count = 10
	print(count)

Myfun()
print(count)

count = 5
def Myfun():
	global count
	count = 10
	print(count)

Myfun()
print(count)
#注意:使用global关键字修饰的变量之前可以并不存在，
#而使用nonlocal关键字修饰的变量在嵌套作用域中必须已经存在。
print("*************************************************")
#nonlocal关键字
def fun_outer():
	count = 999
	def fun_inner():
		nonlocal count
		count = 333
	fun_inner()
	print("inner:",count)
fun_outer()#输出333，如果去掉nonlocal count，则输出999













































































