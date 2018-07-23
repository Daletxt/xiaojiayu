print('hello,world')

class int(int):
	def __add__(self,other):
		return int.__sub__(self,other)

a = int('5')
b = int(3)
print(a,b)
print(a+b)

print('**********************************')

class Nint(int):
	def __radd__(self,other):
		return int.__sub__(self,other)

c = Nint(5)
d = Nint(3)
print(c+d,1+d,type(1),type(d))

#此处c+d为什么不是8，而是2，（删掉上边的int重新启动程序，则会是8）并不是因为类Nint的反运算，
#而是执行了上边int的重载的__add__方法，因为
#当一个类实现了__add__的时候，将会掩盖__radd__方法，也就是__add__的优先度更高

#重写反运算时注意顺序问题
class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(self,other)

a = Nint(5)
print(3-a)


class Nint(int):
	def __rsub__(self,other):
		return int.__sub__(other,self)

a = Nint(5)
print(3-a)
























































































