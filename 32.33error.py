print('hello,world')
file_name = input('请输入要打开的文件名：')
f = open(file_name)
print('文件的内容是：')
for each_line in f:
	print(each_line)

try:
	
	sum = 1 + '1'#跳到TypeError那行执行，之后便停止，只能报出一个错误
	f = open('我为什么是一个文件.txt')
	print(f.read())
	f.close()
	
except TypeError as reason:
	print('类型出错啦\n错误的原因是：'+ str(reason))	
except OSError as reason:
	print('文件出错啦\n错误的原因是：'+ str(reason))

except(TypeError,OSError):
	print('出错了，文件或类型错误！')#判读多个错误

except:
	print('出错啦')#所有错误都会报'出错啦'，用户体验好，不推荐，会隐藏程序员未想到、未准备好处理的错误


	
try:
	f = open('我为什么是一个文件.txt','x')
	print(f.write('我存在了！'))
	sum = 1 + '1'
except(OSError,TypeError):
	print('出错啦！')
finally:#无论如何 都会被执行的代码
	f.close()

	
#引发异常
raise ZeroDivisionError('主动引发一个除数为0的异常')




















































































