print('hello,world')

string = "python"
it = iter(string)
while True:
	try:
		each = next(it)
	except StopIteration:
		break
	print(each)

for each in "python":
	print(each)

class Fibonacci:
	def __init__(self,n = 100):
		self.a = 0
		self.b = 1
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > self.n:
			raise StopIteration
		return self.a
f = Fibonacci()
for each in f:
	if each < 50:
		print(each)
	else:
		break

f = Fibonacci()
for each in f:
		print(each)




























































































