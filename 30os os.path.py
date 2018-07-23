print('hello,world')

import os
os.getcwd()#获取当前路径
os.chdir('D:/Python')#改变路径
os.listdir()#列出当前路径下的所有文件名
os.mkdir('D:\\Python/S')#创建单层目录，如该目录已存在抛出异常
#os.remove('D:/Python/remove.txt')
os.makedirs('D:/Python/S/A/B')
#os.removedirs('D:/Python/S')#非空，抛出异常
#os.removedirs('D:/Python/S/A')#非空，抛出异常
os.removedirs('D:/Python/S/A/B')

os.makedirs('D:/Python/S/A/B')
os.makedirs('D:/Python/S/A/B1')
os.removedirs('D:/Python/S/A/B')#此时只能删除B目录，删不掉B1目录
os.rename('D:/Python/S/A/B1','D:/Python/S/A/B.rename')#将文件重命名
os.system('cmd')#运行系统的shell命令
os.curdir#指代当前目录（‘.’）
os.listdir(os.curdir)
os.pardir#指代上一级目录（‘..’）
os.sep#输出操作系统特定的路径分隔符（Win下为‘\\’,Linux下为‘/’）
os.linesep#当前平台使用的行终止符（Win下为‘\r\n’,Linux下为‘/’）
os.name#指代当前使用的操作系统（包括：‘posix’，‘nt’，‘mac’，'os2','ce','java'）

os.path.basename("D:/Python/S/A/B/haha.exe")#去掉目录路径，单独返回文件名
os.path.dirname("D:/Python/S/A/B/haha.exe")#去掉文件名，单独返回目录路径
os.path.join("D:\\","a","b","c")#将各部分组合成一个路径名
os.path.split("D:\\s\\a\\b\\c")#分离文件名与扩展名，返回（f_name,f_extension）元组
os.path.split("D:\\s\\a\\b\\c.exe")
os.path.getatime('D:\\Python\\record.txt')
#返回指定文件的最近访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
os.path.getctime('D:\\Python\\record.txt')#。。。创建时间。。。
os.path.getmtime('D:\\Python\\record.txt')#。。。最新修改时间。。。

os.path.exists('D:\\Python\\record.txt')#判断指定路径（目录或文件）是否存在
os.path.isabs('D:\\Python\\record.txt')#判断指定路径是否为绝对路径
os.path.isabs('.\\Python\\record.txt')
os.path.isabs('.\\record.txt')
os.path.isdir('D:\\Python\\record.txt')#。。。是否存在 且是一个目录
os.path.isfile('D:\\Python\\record.txt')#。。。是否存在 且是一个文件
os.path.islink('D:\\Python\\record.txt')#。。。是否存在 且是一个符号链接（win快捷方式）
os.path.ismount('D:\\')#。。。是否存在 且是一个挂载点（硬盘盘符）
os.path.samefile('D:\\Python\\record.txt','D:\\Python')#判断两个路径是否指向同一文件







































































