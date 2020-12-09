# 一、递归：是一种编程思维，遍历一个文件
# 递归的特点：函数内部自己调取自己，必须有出口
'''
def test(num):
    if num == 1:
        return num
    return num + test(num -1)
sum_num = test(3)
print(sum_num)
'''
# 二、lambda表达式：如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
# lambda 参数列表：表达式
'''
def fel():
    return 200
print(fel())
print(fel) # 直接调取函数名，打印的时函数的内存地址
fel2 = lambda: 200
print(fel2)
print(fel2()) # 直接调取函数名，打印的时函数的内存地址
'''
# 计算a + b
'''
def add_num(a,b):
    return a + b
print(add_num(2,3))

add_num2 = lambda a,b:a + b
print(add_num2(1,3))
'''
# lambda的参数形式
'''
# 无参数
test0 = lambda: 100
print(test0())
# 一个参数
test1 = lambda a: 200
print(test1(12))
# 默认参数
test2 = lambda a,b,c = 500: a + b + c
print(test2(300,400))
# 可变参数 *args
test3 = lambda *args: args
print(test3('Tom',8,'男'))
# 可变参数 **kwargs
test4 = lambda **kwargs: kwargs
print(test4(name='Rose',age=18))
'''
# lambda 的应用
# 带判断的lambda
'''
test5 = lambda a, b: a if a > b else b
print(test5(3, 4))
'''
# 列表数据按字典key的值排序
'''
students = [{'name': 'Tom', 'age': 18}, {'name': 'Rose', 'age': 19}, {'name': 'Jack', 'age': 16}]
students.sort(key=lambda a: a['name'])
print(students)
students.sort(key=lambda a: a['name'], reverse=True)
print(students)
'''
# 三、高阶函数
# 高级函数：把函数作为一个参数传入
# ads 绝对值的计算
abs(-1)
print(abs(-1))
# round() 完成数字的四舍五入
round(8.9)
print(round(0.9))
# 需求：任意两个数字，按照指定要求整理理数字后再进⾏行行求和计算。
'''
def add_num(a,b):
    return abs(a) + abs(b)
result = add_num(3,-9)
print(result)
def add_num(c,d,e):
    return e(c) + e(d)
result1= add_num(2,3,abs)
print(result1)
'''
# 内置高阶函数
# map(funs,lst):将传入的函数变量funs作用到lst变量的每个元素中
'''
list1 = [1,2,3,5]
def funs(a):
    return a **2
result = map(funs,list1)
print(result)
print(list(result))
'''
# reduce(func,lst):funs必须y有两个参数,每次funs计算的结果和序列的下一个元素做累积计算
'''
import functools
list2 = [1,2,4,5]
def add_num(a,b):
    return a + b
result = functools.reduce(add_num,list2)
print(result)
'''
# filter():过滤列表
list3 = [1,2,4,5,6,7,8]
def funs(a):
    return a%2 == 0
result = filter(funs,list3)
print(list(result))