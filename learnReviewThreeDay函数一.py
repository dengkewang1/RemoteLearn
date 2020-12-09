# 函数的定义、使用、参数的作用、返回值、说明文档、函数的嵌套、函数的作用

#  1、函数的定义及使用
"""
def add_num():
    '''定义一个函数'''
    result = 1 + 2
    print(result)
# 使用函数
add_num()
'''
函数的定义
def 函数名(参数):
    代码
'''
'''
函数的使用
函数名()
'''
def add_num1(a,b):
    result1 = a + b
    print(result1)
number1 = int(input('请输入第一个数字：'))
number2 = int(input('请输入第二个数字：'))
add_num1(number1,number2)
"""
# 2、函数的返回值
"""
def buy():
    return '烟'
good = buy()
print(good)
# 需求：制作⼀一个计算器器，计算任意两数字之和，并保存结果。
def add_calculator(a,b):
    result = a + b
    return result
input_add_num = add_calculator(1,2)
print(input_add_num)
"""
# 3、函数的说明文档
"""
# 定义函数的说明文档
def 函数名():
    '''说明文档的位置及内容'''
    代码
# 查看说明文档
help(函数名)
"""
"""
def add_num(a,b):
    '''定义一个求和函数'''
    return a + b
help(add_num)
"""
# 4、函数嵌套调用：一个函数中可以调用另一个函数
"""
def testb():
    print('----testB start----')
    print('testB')
    print('----testB end----')
def testA():
    print('----testA start----')
    testb()
    print('----testA start----')
testA()
"""
# 7、函数应⽤用
# 7.1 打印图形
"""
# 1. 打印⼀一条横线
'''
def line():
    print('_*' * 5)
line()
'''
# 2. 打印多条横线
# 2.1 函数内直接打印
'''
def lines():
    i = 0
    while i < 5:
        print('_*' * 5)
        i += 1
lines()
'''
# 2.2 函数嵌套打印
def line(j):
    print(f"第{j}行{'_*' * 5}")
def line1(num):
    i = 1
    while i <= num:
        j = i
        line(j)
        i += 1
a = int(input('请输入打印行数：'))
line1(a)
"""
# 7.2 函数计算
# 1. 求三个数之和
def three_add(num1,num2,num3):
    return num1 + num2 + num3
"""
a = int(input('输入第一个数：'))
b = int(input('输入第二个数：'))
c = int(input('输入第三个数：'))
sum1 = three_add(a,b,c)
print(sum1)
"""
# 2. 求三个数平均值
def three_average(NUM1,NUM2,NUM3):
    ADD = three_add(NUM1,NUM2,NUM3)
    return ADD/3
a = int(input('输入第一个数：'))
b = int(input('输入第二个数：'))
c = int(input('输入第三个数：'))
average = three_average(a,b,c)
print(int(average))