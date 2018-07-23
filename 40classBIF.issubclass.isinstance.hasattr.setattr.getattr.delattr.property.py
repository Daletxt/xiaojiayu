print('hello,world')
#类和对象一些相关的BIF

#issubclass(class,classinfo)检查class是否是classinfo的子类，非严格性，
#1.一个类被认为是其自身的子类
#2.classinfo可以是类对象组成的元组，只要class是其中任何一个候选类的子类，则返回True
class A:
	pass
class B(A):
	pass

print("B是A的子类吗",issubclass(B,A))
print("B是B的子类吗",issubclass(B,B))
print("A是B的子类吗",issubclass(A,B))
print("A是元组(A,B)的子类吗",issubclass(A,(A,B)))
print("B是object的子类吗",issubclass(B,object))#object是所有类的一个基类

class C:
	pass

print("B是C的子类吗",issubclass(B,C))
print()

#isinstance(object,classinfo)检查一个实例对象object是否属于类classinfo
#1.如果第一个参数不是对象，则永远返回False
#2.如果参数不是类或者由类对象组成的元组，会抛出一个TypeError异常
b1 = B()
print("b1属于B类吗",isinstance(b1,B))
print("b1属于A类吗",isinstance(b1,A))
print("b1属于C类吗",isinstance(b1,C))
print("b1属于元组(A,B,C)吗",isinstance(b1,(A,B,C)))
print()

#hasattr(object,name)检查一个对象object是是否有指定的‘name’属性(属性名需要“name”)
class C:
	def __init__(self,x=0):
		self.x = x

c1 = C()
print("x属性是否在实例化对象d1中",hasattr(c1,'x'))
#print("x属性是否在实例化对象d1中",hasattr(c1,x))
#NameError: name 'x' is not defined
print("y属性是否在实例化对象d1中",hasattr(c1,'y'))
print()

#getattr(object,name[,default])返回对象object指定的属性‘name’值
print('实例化对象c1中x属性的值为：',getattr(c1,'x'))
#print('实例化对象c1中y属性的值为：',getattr(c1,'y'))
#AttributeError: 'C' object has no attribute 'y'
print('实例化对象c1中y属性的值为：',getattr(c1,'y','您所访问的属性不存在...'))
print()

#setattr(object,name,value)设置对象object中指定属性‘name’的值，不存在则创建新的
setattr(c1,'y',['FishC',7])
print('实例化对象c1中y属性的值为：',getattr(c1,'y','您所访问的属性不存在...'))

#delattr(object,name)删除对象object中指定的属性‘name’，不存在则抛出异常
delattr(c1,'y')
#delattr(c1,'y')
#AttributeError: y
try:
	delattr(c1,'y')
except AttributeError:
	print('删除实例化对象的属性y异常')

#property(fget=None,fset=None,fdel=None,doc=None)通过属性设置属性
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

c1 = C()
print(c1.getSize())
print(c1.x)
c1.x = 18
print(c1.x)
print(c1.size)
print(c1.getSize())
del c1.x
print(c1.size)









































