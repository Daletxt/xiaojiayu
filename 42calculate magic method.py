print('hello,world')

print(type(len))
print(type(dir))
print(type(int))
print(type(list))
class C:
	pass

print(type(C))
a = int('123')
b = int('456')
print(a+b)
#Python的魔法方法自定义任何算数运算
class New_int(int):
	def __add__(self,other):	#重新魔法方法__add__加变减
		return int.__sub__(self,other)
	def __sub__(self,other):	#重新魔法方法__sub__减变加
		return int.__add__(self,other)
a = New_int(3)
b = New_int(5)
print(a+b)
print(a-b)
print(a*b)
a,b = 3,5
print(a+b)



class Try_int(int):
	def __add__(self,other):
		return self + other
	def __sub__(self,other):
		return self - other

a = Try_int(3)
b = Try_int(5)
#print(a+b)#产生无限递归

class Try_int(int):
	def __add__(self,other):
		return int(self) + int(other)
	def __sub__(self,other):
		return int(self) - int(other)

a = Try_int(3)
b = Try_int(5)
c = Try_int(10)
print(a+b+c)

#工厂函数

















































































