#创建和访问字典
#1.传统的文字表达式
a = {'name':'Dale','age':'18','gender':'male'}
print(a)
#2.动态分配键值
b = {}
b['name'] = 'Amy'
b['age'] = 18
b['gender'] = 'female'
print(b)
#3.字典键值表
c = dict(name='John',age=14,gender='male')
print(c)
#4.字典键值元组表
d1 = dict([('name','Jack'),('age',14),('gender','male')])
d2 = dict((('name','Jac'),('age',1),('gender','mal')))
print(d1,d2)
#5.所有键的值都相同或者赋予初始值
e = dict.fromkeys(['height','weight'],'normal')#后者参数可选，不给则默认"None"
print(e)

#访问字典
for eachkey in a.keys():
    print(eachkey)
for eachvalue in a.values():
    print(eachvalue)
for eachitem in a.items():
    print(eachitem)

#print(a['nam']) 访问不存在的键会报错
print(b.get('nam'))
print(b.get('nam','没有这个东东'))#设置没有的键时返回值
print(b.get('name','没有这个东东'))
print('name' in a)
print('agee' in a)

#清空字典e.clear()不同于e = {}
f = e
print(e,f)
e = {}
print(e,f)
f = e
e.clear()
print(e,f)

g = a.copy()
h = a   #在相同的数据上贴了一个不同的标签
print('字典a地址：',id(a))
print('前拷贝：g地址 = a.copy()：',id(g))
print('赋值：h地址 = a：',id(h))
print(h.pop('gender'))
print(a)
print(g)
print(h)
print(h.popitem())#随机删，因为字典没顺序
print(h)
h.setdefault('小白')
h.setdefault('animal','小嘿')
print(a)
i = {'小白':'狗'}
a.update(i)#更新字典
print(a)



































































