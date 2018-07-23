#集合
num = {}
print(type(num))
num2 = {1:1.1,2:2.2,3:3.3}
print(type(num2))
num3 = {1,2,3,4,5,5,5}
print(num3,type(num3))
#集合重复的元素自动被剔除，元素具有唯一性，无序，不支持索引index
#创建集合
#1.如上
#2.set()
set1 = set([1,2,3,4,5,5])
print(set1)
#去掉列表中重复的元素
num4 = [1,2,3,4,5,5,3,1,0]
temp = []
for each in num4:
    if each not in temp:
        temp.append(each)
print(temp)

num5 = list(set(num4))#集合元素无序
print(num5)

#访问集合中的值
print(1 in num3)
print("1" in num3)
num3.add(6)
print(num3)
num3.remove(5)
print(num3)

#不可变集合
num6 = frozenset(num3)
print (num6)
print(type(num6))
#num6.add(5),报错，不可变集合不可变AttributeError: 'frozenset' object has no attribute 'add'

 









































































