'''
#导入方法1：import 模块名
import TemperatureConversion
print("32摄氏度 = %.2f华氏度" % TemperatureConversion.c2f(32))
print("99华氏度 = %.2f摄氏度" % TemperatureConversion.f2c(99))

#导入方法2：from 模块名 import 函数名 ：节省命名空间 使代码更为简洁
from TemperatureConversion import c2f,f2c
print("32摄氏度 = %.2f华氏度" % c2f(32))
print("99华氏度 = %.2f摄氏度" % f2c(99))

#from TemperatureConversion import *#(通配符)方式导入，不建议使用，易导致命名空间混乱
'''

#导入方法3：import 模块名 as 新名字(推荐)
import TemperatureConversion as tc
print("32摄氏度 = %.2f华氏度" % tc.c2f(32))
print("99华氏度 = %.2f摄氏度" % tc.f2c(99))
