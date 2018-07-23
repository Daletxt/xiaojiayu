print('hello,world')

def myGen():
	print("生成器被执行！")
	yield 1
	yield 2

m = myGen()

print(next(m))

print(next(m))

#print(next(m))
#StopIteration

for i in myGen():
	print(i)

def fibs():
	a = 0
	b = 1
	while True:
		a,b = b,a+b
		yield a

for each in fibs():
	if each > 100:
		break
	print(each,end = ' ')

#列表推导式
a = [i for i in range (32) if not (i % 2) and i %3]
print(a)
#字典推导式
b = {i:i % 2 == 0 for i in range(10)}
print(b)
#集合推导式
c = {i for i in [1,3,2,4,3,2,4,5]}
print(c)
#
d = "i for i in 'I love python！'"
print(d)
#生成器推导式
e = (i for i in range(10))
print(e)

print(next(e))
print(next(e))
print(next(e),'停')

for each in e:
	print(each)

print(sum(i for i in range(100) if i % 2))
print(sum((i for i in range(100) if i % 2)))
































































