
def ds(x):
	return 2 * x + 1

print(ds(5))

#匿名函数
g = lambda x : 2 * x + 1
print(g(5))



def add(x,y):
	return x + y
print(add(3,4))

#匿名函数 lambda可以省下定义函数过程，使代码更加简洁；不需要考虑函数命名问题；简化代码可读性。
f = lambda x,y: x + y
print(f(3,4))

#内置函数：过滤器 filter()
from collections import Iterator
a = filter(None,[1,0,False,True,5])#filter过滤出True类型
print(list(a))
print(type(a))
print(isinstance(a,filter))
print(isinstance(a,Iterator))#filter是可迭代对象

def odd(x):
	return x % 2

temp = range(10)
show = filter(odd,temp)
print(list(show))

#用filter、lambda写：
print(list(filter(lambda x : x % 2 == 0,range(10))))

#内置函数：映射 map()
print(list(map(lambda x : x * 2,range(10))))
















































































