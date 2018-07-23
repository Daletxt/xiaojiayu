print('hello,world')

class Parent:
	def hello(self):
		print("正在调用父类的方法（函数）...")

class Child(Parent):
	pass

p = Parent()
p.hello()
c = Child()
c.hello()

class Child(Parent):
	def hello(self):
		print('正在调用子类的方法...')

c = Child()
c.hello()
p.hello()

import random as r
class Fish:
	def __init__(self):
		self.x = r.randint(0,10)
		self.y = r.randint(0,10)
	def move(self):
		self.x -= 1
		print("我的位置是：",self.x,self.y)
class Goldfish(Fish):
	pass

class Carp(Fish):
	pass

class Salmon(Fish):
	pass

class Shark(Fish):
	def __init__(self):
		self.hungry = True

	def eat(self):
		if self.hungry:
			print("吃货的梦想就是天天有的吃")
			self.hungry =  False
		else:
			print("太撑了，吃不下了")

fish = Fish()
fish.move()
fish.move()
goldfish = Goldfish()
goldfish.move()
goldfish.move()
shark = Shark()
shark.eat()
shark.eat()
#shark.move()
#AttributeError: 'Shark' object has no attribute 'x'

#解决此问题：
class Shark(Fish):
	def __init__(self):
		Fish.__init__(self)	#①：调用未绑定的父类的方法
		self.hungry = True

shark = Shark()
shark.move()
Fish.__init__(shark)
#Fish.__init__()
#TypeError: __init__() missing 1 required positional argument: 'self
shark.move()

class Shark(Fish):
	def __init__(self):
		super().__init__()	#②：super函数，自动找到基类的方法并传入self参数
		self.hungry = True
#super()函数超级之处是：不用给定任何基类的名字，优于方法①
shark = Shark()
shark.move()

class Base1:
	def foo1(self):
		print("我是foo1，我为Base1代言...")

class Base2:
	def foo2(self):
		print("我是foo2，我为Base2代言...")

class C(Base1,Base2):
	pass

c = C()
c.foo1()
c.foo2()
#当不确定是否必须用多重继承语法时，尽量避免使用，因为有时会出现不可预见的bug














































































