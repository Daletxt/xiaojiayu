def fun1():
	print('fun1正在被调用...')
	def fun2():
#内嵌函数，定义和调用过程都在fun1中，出了fun1，就没有对fun2进行调用的方式了
		print('fun2正在被调用...')
	fun2()
fun1()
#fun2()	报错 NameError: name 'fun2' is not defined


#闭包：函数式编程的一个重要的语法结构。
def FunX(x):
	def FunY(y):
		return x * y
	return FunY

i = FunX(8)
type(i)
print(i(5))
print(FunX(8)(5))
#FunY(5)报错

'''
def Fun1():
	x = 5
	def Fun2():
		x *= x
		return x
	return Fun2()
print(Fun1())
报错
'''
def Fun1():
	x = [5]
	def Fun2():
		x[0] *= x[0]
		return x[0]
	return Fun2()
print(Fun1())

#nonlocal关键字
def Fun1():
	x = 5
	def Fun2():
		nonlocal x
		x *= x
		return x
	return Fun2()
Fun1()


















































































