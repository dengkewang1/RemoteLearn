# 一、变量的作用域
# 分为 局部变量、全局变量
# 局部变量
'''
def testA():
    a = 100
    print(a)
testA()
# print(a) # NameError: name 'a' is not defined
'''
# 全局变量————局部变量与全局变量的不同调用
"""
b = 100
'''全局变量'''
def testB():
    b = 200
    '''局部变量'''
    print(b)
print(b)
testB()
"""
# 函数内定义全局变量————global
"""
c = 50
def testC1():
    print(c)
def testC():
    global c
    c = 100
    print(c)
testC1()
testC()
print(f'{c}')
"""
# 二、多函数程序执行流程
# 公用局部变量
'''
glo_num = 10
def test1():
    global glo_num
    glo_num = 100
def test2():
    print(glo_num)
test1()
test2()
'''
# 返回参数作为参数传递
'''
def test1():
    return 50
def test2(num):
    print(num)
a = test1()
test2(a)
'''
# 三、函数的返回值
# 一个函数有多个返回值：return返回多个数据默认是元组，return后面可以连接列表、元组、字典
'''
def test1():
    return 1, 2
result = test1()
print(result)
print(type(result))
'''
# 四、函数的参数
# 位置参数：调用函数时根据函数定义的位置传递
'''
def user_info(name,age,gender):
    print(f'名字：{name}，年龄：{age}，性别：{gender}')
user_info('Tom','18','男')
'''
# 关键字参数：调用函数通过‘键 = 值’形式加以指定。如果调用时有位置参数，位置参数必须在关键字参数的前面，关键字参数之间不存在先后顺序
'''
def user_info(name,age,gender):
    print(f'名字：{name}，年龄：{age}，性别：{gender}')
user_info('Tom',age='18',gender='男')
user_info('Rose',gender='女',age='23')
user_info(gender='男',name='小米',age='24')
'''
# 缺省参数————又叫默认参数：所有位置参数必须出现在默认参数前面，包括定义及调用
'''
def user_info(name,age,gender='男'):
    print(f'名字：{name}，年龄：{age}，性别：{gender}')
user_info('Tom','18')
user_info('Rose','20','女')
'''
# 不定长参数————包裹传递，无论时位置传递还是关键字传递，都是一个组包的过程
# 包裹位置传递：*args 传进的所有参数都会被args变量收集，会根据传进参数的位置合并为一个元组
# args时元组类型，这就是包裹传递
'''
def user_info(*args):
    print(*args)
user_info('Tom',18,'男')
'''
# 包裹关键字传递：**kwargs 传进的所有参数都会被kwargs变量收集，会根据传进参数的位置合并为一个字典
'''
def user_info(**kwargs):
    print(kwargs)
user_info(name='Rose',age=18,gender='女')
'''
# 五、拆包和交换变量值
# 拆包元组
'''
def return_num():
    return 100, 200
num1,num2 = return_num()
print(num1)
print(num2)
'''
# 拆包字典
'''
dict1 = {'name': 'TOM', 'age': 18}
a, b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])
'''
# 交换变量值
# 借助第三个变量存储数据
'''
a = 1
b = 2
c = 0
c = a
a = b
b = c
print(a)
print(b)
'''
# 方法二
'''
a,b = 1,2
a,b = b,a
print(a,b)
'''
# 六、引用
# int类型：不可变类型
'''
a = 1
b = a
print(id(a))
print(id(b))
a = 2
print(id(a))
print(id(b))
'''
# 列表
aa = [10,20]
bb = aa
print(id(aa))
print(id(bb))
aa.append(30)
print(id(aa))
print(id(bb))
# 七、可变和不可变类
# 不可类型
int
float
str
tuple
# 可变类型
list
dict
set