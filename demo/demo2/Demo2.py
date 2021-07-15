# Filename: 2emo2.py
import sys
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

if __name__ == "__main__":
    print('\n\nPython 路径为：', sys.path, '\n')



"""
while True:
    try:
        print(next(myiter))
    except StopIteration:
        sys.exit()

for i in myiter:
    if i == 51:
        print(" ")
    print(i,end=" ")
"""
"""
使用 迭代器返回斐波那锲数列

def fibonacci(n):   #生成器
    a,b,count = 0,1,0
    while True:
        if (count) > n:
            return
        yield a
        a,b = b,a + b
        count += 1

#创建一个迭代器
f = fibonacci(20)
print(f)
#遍历迭代器
while True:
    try:
        j = 0
        for i in f:
            print("第",j,"个元素为：",i,"\n")
            j += 1
    except StopIteration:
        sys.exit()
"""

"""
自定义函数
#计算面积函数
def area(width,height):
    return width*height

a = 4
b = 6
print("宽为：",a,"高为：",b,"面积为：",area(a,b))
"""
def area(width,height):
    return width*height

"""
传不可变对象
def ChangeInt(b):
    b.append([1,2,3,4])
    print(id(b))
    return  b
b = [1,4,6,2]
print(id(b))
ChangeInt(b)
print(b)
"""
"""
关键字参数

def printme(name,age,*,c):
    print("名字：",name)
    print("年龄：",age)
    print(c)
    return
#调用函数
printme("李志林",25,c='假的')
"""
"""
lambda匿名函数
sum = lambda str1,str2 : str1 + str2
print(sum("hello"," world"))
print(sum(10,20))
"""

"""
强制位置参数
def f(a, b, /,c, d, *, e, f):
    print(a, b, c, d, e, f)
f(10,20,c=30,d=40,e=50,f=60)
"""
"""
m = [34,12,5,88,12,46,33,56.3,9]
#计算元素出现的次数
print("元素3出现的次数为：",m.count(12))

#增加元素
m.insert(2,63)
m.append(70)
print(m)

#获取元素索引
print(m.index(12))

#删除元素
m.remove(12)
print(m)

#列表排序-正序
m.sort()
print(m)

#列表排序-倒序
m.reverse()
print(m)
"""

#使用pop()方法释放最后一个元素
"""
m.pop()
print(m)
m.pop()
print(m)
"""

"""
将集合变成队列
from _collections import deque
queue = deque(m)
print(queue.popleft())
print(m)
"""

"""
嵌套列表
n = [3+x for x in m if x > 10]
print(n)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
a=[x*y for x in vec1 for y in vec2]

b=[x+y for x in vec1 for y in vec2]

c=[vec1[i]*vec2[i] for i in range(len(vec1))]
print(a)
print(b)
print(c)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12]]
d = [[row[i] for row in matrix] for i in range(4)]
print(d)
"""

"""
t = 12345,45242,"hello"
u = t,(1,2,3,4,5)
print(u)

#遍历字典
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for x,y in knights.items():
    print(x,y)

#同时获取列表元素和下标
a = ["abc","as","rrt","hgs","klg"]
for i,x in enumerate(a):
    print(i," ",x)
#同时遍历多个列表
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for x,z in zip(questions,answers):
    print("What is your {0}, It is {1}".format(x,z))

for i in reversed(range(1,10,2)) :
    print(i)

for i in sorted(a):
    print(i)
"""

"""
rjust用法
"""
for n in range(1,11):
    print(repr(n),repr(n*n).rjust(10),end=" ")
    print(repr(n*n*n).rjust(10))


import random
print(''.join(random.sample('1234567890abcdefghijklmn',9)))

for n in range(10):
    print("这个值为：%d"%n)