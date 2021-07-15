# 导入模块
import sys
import demo2.Demo2
#from 2emo2 import area
print("长方形的面积为：",demo2.Demo2.area(4,5))
print("该模块内定义的所有名称为有：",dir(sys))

print("我叫 %s 今年 %d 岁!，我喜欢打 %s" % ('小明', 10, "篮球"))

# 遍历
for x in [1, 2, 3]:
    print(x, end=" ")

print("\n")
listmap = {"str1": "李", "str2": "志", "str3": "林", "str4": "24", "str5": "唱歌"}

listmap.pop("str5")

print(listmap)

# listmap2 = listmap.get("str2")
listmap3 = listmap.items()
for i, j in listmap3:
    print("键为:" + i + "，值为：" + j)
print(listmap.items())

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("pear" in basket)
print(basket)

a = set('abracadabra')
b = set('alacazam')
print(a, b)
# a-b  a包含而b不包含的元素
print(f'a-b的结果为：{a - b}')

# 集合a或b中包含的所有元素
print(f'a | b的结果为：{a | b}')

# 集合a和b中都包含了的元素
print(f'a&b的结果为：{a & b}')

# 不同时包含于a和b的元素
print(f'a^b的结果为：{a ^ b}')

c = {x for x in a if x not in 'abc'}
print(c)

a.add("f")
a.update({2, 5})
a.update(['t', '3', 'y'])
a.pop()
print(f'a的值为：{a}')
print(f'a集合元素的个数为：{len(a)}')

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
m, n = 0, 1
while n < 10000:
    if (n % 2 == 0):
        print(f'偶数n为：{n}')
    print(n, end=",")
    m, n = n, m + n

var1 = 100
if var1:
    print("1 - if 表达式条件为 true")
    print(var1)

var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

# 计算狗狗年龄
'''
age = int(input("请输入你家狗狗年龄："))
if age <= 0:
    print("你是在逗我吧")
elif age ==1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age-2)*5
    print("对应人类的年龄为：",human)
###退出提示
input("点击 enter 键退出")
'''

"""
猜数字游戏
number = 6
guess = -1
while guess != number:
    guess = int(input("请输入你要猜的数字："))

    if guess == number:
        print("恭喜你猜对了，数字是：",guess)
        break
    elif guess > number:
        print("你猜的数字大了")
    elif guess < number:
        print("你猜的数字小了")
"""

"""
if elif else 嵌套
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")
"""

"""
计算1~30,第一天金额为0.01元，之后每天增长前一天的2倍，每一天的金额已经30天的总金额
n = 30
sum = 0
todaySum = 0.01
count = 1
while count <= n:
    if count == 1:
        sum = todaySum
    else:
        todaySum = todaySum*2
        sum += todaySum
    print(f'第{count}天的金额为：{todaySum}')
    count += 1

print("30天的总金额为：%d"%(sum))
"""

"""
无线循环
var = 1
while var == 1:
    num = int(input("请输入一个数字："))
    print("你输入的数字为：",num)
"""

"""
for break语句
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程")
        break
    print("循环数据为：",site)
else:
    print("没有循环数据")
print("完成循环")
"""

"""
range()函数

str = ["abc","bba","ccd","ffj","ppd"]
for i in range(len(str)):
    print(i,str[i])

strlist = list(range(5))

print(strlist)
"""

"""
while-break-continue-else 语句
"""
"""
迭代器
"""
listStr = [1, 5, 4, 2, 6, 7, 3]
# 创建一个迭代器
it = iter(listStr)
# 循环遍历迭代


while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
