def MyFirstFunction():
	print('这是我创建的第一个函数！')
	print('我表示很鸡冻。。。')
	print('在此，我要感谢CCAV。。。')
MyFirstFunction()		#调用自定义函数


def MySecondFunction(name):		#参数可变，name
	print(name + "我爱你！")
MySecondFunction('小鱿鱼')


def add(num1,num2):
	result = num1 + num2
	print(result)
add(2,4)


def add(num1,num2):
		return (num1 + num2)
print(add(5,6))


def canshu(name):
	'函数定义过程中的name是叫形式参数，形参'
	#因为Ta只是一个形式，表示占据一个参数位置
	print('传递进来的'+ name +'叫做实参，因为Ta是具体的参数值！')
canshu("小红帽")
print(canshu.__doc__)
help(canshu)
'''
>>>print.__doc__
>>>help(print)
'''
print("****************************************")

def SaySome(name,words):
	print(name + "说过->" + words)
SaySome('小甲鱼','让编程改变世界！')
SaySome('让编程改变世界！','小甲鱼')
SaySome(words = '让编程改变世界！',name = '小甲鱼')#使用关键字参数


def DoSome(name = '上帝',thing = '羊'):#默认参数
	print(name + "创造了" + thing)
DoSome()#忘了传参数，调用默认参数，防止出错
DoSome('苍井空')
DoSome('羊驼','上帝')
DoSome(thing = '羊驼',name = '上帝')
#在参数调用中，通过参数名定制需要赋值的参数，
#就不怕因为搞不清参数顺序，而导致函数调用出现莫名其妙的错误

print("****************************************")

#收集参数（可变参数）（不定长参数）
def test(*params,exp = 88):
#在可变参数后的参数设定默认参数，在调用是不易出错
	print('参数的长度是：',len(params),exp);
	print('第二个参数是：',params[1]);
test(1,'小甲鱼',3.14,5,6,7,"你好")#若没有默认参数88则报错
test(1,'小甲鱼',3.14,5,6,7,exp = "你好")










































