print('hello,world')

class Turtle:
	def __init__(self,x):
		self.num = x

class Fish:
	def __init__(self,x):
		self.num = x
#使用组合，不使用继承，将需要的类实例化放到新类里即可
class Pool:
	def __init__(self,x,y):
		self.turtle = Turtle(x)
		self.fish = Fish(y)

	def print_num(self):
		print('水池里总共有乌龟 %d 只，小鱼 %d 条！' % (self.turtle.num,self.fish.num))

pool = Pool(1,10)
pool.print_num()

#类vs类对象vs实例对象：类中定义的属性为静态属性，类属性和类对象相互绑定，不依赖实例对象，
#操作实例对象时不会影响类属性

class C:
	def x(self):
		print("X-man!")

c = C()
c.x()
c.x = 1
print(c.x)
#c.x()
#TypeError: 'int' object is not callable
#属性名和方法名相同，则属性会把方法覆盖掉，所以：

#不要试图在一个雷里定义出所有能想到的特性和方法，应该利用继承和组合的机制来进行扩展。
#用不同词性命名（约定俗成），如属性名用名词，方法名用动词

#Python严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓绑定概念。











































































