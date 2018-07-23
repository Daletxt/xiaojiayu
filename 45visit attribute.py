print('hello,world')

class C:
	def __init__(self):
		self.x = 'X-man'

c = C()
print(c.x)

print(getattr(c,"x",'没有这个属性！'))

print(getattr(c,"y",'没有这个属性！'))

print("***********************************")

class C:
	def __init__(self,size=10):
		self.size = size
	def getSize(self):
		return self.size
	def setSize(self,value):
		self.size = value
	def delSize(self):
		del self.size
	x = property(getSize,setSize,delSize)

c = C()
c.x = 1
print(c.x,c.size)
del c.x
#print(c.x,c.size)
#AttributeError: 'C' object has no attribute 'size'
print("***********************************")
'''
__getattr__(self,name)定义当用户试图获取一个不存在的属性时的行为
__getattribute__(self,name)定义当该类的属性被访问时的行为
__setattr__(self,name,value)定义当一个属性被设置时的行为
__delattr__(self,name)定义当一个属性被删除时的行为
'''

class C:
	def __getattribute__(self,name):
		print("getattribute")
		return super().__getattribute__(name)
	def __getattr__(self,name):
		print("getattr")
	def __setattr__(self,name,value):
		print("setattr")
		super().__setattr__(name,value)
	def __delattr__(self,name):
		print("delattr")
		super().__delattr__(name)

c = C()
print(c.x)
c.x = 1
print(c.x)
del c.x
print(c.x)
#以上和在Python Shell里运行结果不同，原因？

print("***********************************")

class Rectangle:
	def __init__(self,width,height=0):
		self.width = width
		self.height = height

	def __setattr__(self,name,value):
		if name == 'square':
			self.width = value
			self.height = value
		else:
			super().__setattr__(name,value)#调用基类
			self.__dict__[name] = value #方法2
			#self.name = value #无限递归循环bug

	def getArea(self):
		return self.width * self.height

r1 = Rectangle(4,5)
print(r1.getArea())
r1.square = 10
print(r1.width,r1.height,r1.getArea())
print(r1.__dict__)











































































