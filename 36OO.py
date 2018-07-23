print('hello,world')
class Turtle:#类首字母大写
#属性
	color = 'green'
	weight = 10
	legs = 4
	shell = True
	mouth = '大嘴'
#方法
	def climb(self):
		print('我在很努力的向前爬。。')
	def run(self):
		print('我在飞快的向前跑。。')
	def bite(self):
		print('咬死你咬死你！！！')
	def eat(self):
		print('有的吃，真满足！')
	def sleep(self):
		print('困了，睡了，晚安')

tt = Turtle()
tt.climb()
tt.sleep()

list1 = [2,1,7,5,3]
list1.sort()
print(list1)
list1.append(9)
print(list1)

class Mylist(list):
	pass#占位符

list2 = Mylist()
list2.append(4)
list2.append(8)
list2.append(5)
list2.sort()
print(list2)

class A:
	def fun(self):
		print('我是小A')
class B:
	def fun(self):
		print('我是小B')

a = A()
b = B()
a.fun()
b.fun()

class Ball:
	def setName(self,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我...'% self.name)
a = Ball()
a.setName('球A')
b = Ball()
b.setName('球B')
c = Ball()
c.setName('土豆')
a.kick()
c.kick()
#面向对象编程
class Ball:
	def __init__(self,name):
		self.name = name
	def kick(self):
		print('我叫%s，该死的，谁踢我...'% self.name)

b = Ball('面条')
b.kick()
#c = Ball()报错

class Person:
	name = '小甲鱼'

p = Person()
print(p.name)
#Python中定义私有变量，只需在变量名或函数名前面加上"_"两个下划线
class Person:
	__name = '小甲鱼2'
	
p = Person()
#p.__name和p.name都会报错

class Person:
	__name = '小甲鱼3'
	def getName(self):
		return self.__name
		
p = Person()
#p.__name报错
print(p.getName())
print(p._Person__name)#伪私有，python把__name改成_类名__隐藏的变量名




































































