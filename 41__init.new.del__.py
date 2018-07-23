print('hello,world')

#__init__(self[,...])
class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getPeri(self):
        return (self.x + self.y) * 2
    def getArea(self):
        return self.x * self.y

rect = Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())

class A:
    def __init__(self):
        return "A fo A-cup"
#a = A()
#TypeError: __init__() should return None, not 'str'

#__new__(cls[,...])返回一个实例对象，平时极少重写，当继承一个不可变类型，并需要修改时用
class CapStr(str):  #继承不可改类型字符串
    def __new__(cls,string):    #实例化前进行的修改
        string = string.upper()
        return str.__new__(cls,string)  #重写__new__

a = CapStr("I love Python!")
print(a)

#__del__(self)当垃圾回收机制起作用时调用此方法
class C:
    def __init__(self):
        print("我是__init__方法，我被调用了...")
    def __del__(self):
        print("我是__del__方法，我被调用了...")

c1 = C()    #我是__init__方法，我被调用了...
c2 = c1
c3 = c2
del c3
del c2
del c1      #我是__del__方法，我被调用了...
#对象生成后，所有对它的引用（有一个变量指向它就是对它的引用）都被del后才会启动垃圾回收机制，
#垃圾回收机制去销毁这个对象时，会自动调用__del__方法



















































































