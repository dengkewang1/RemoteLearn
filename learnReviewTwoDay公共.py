# 公共操作
"""
#运算符
# +：合并——字符、列表、元组
# 字符串
strPublic = 'dengke'
strPublicTwo = 'wang'
strPublicSumMerge = strPublic + strPublicTwo
print(strPublicSumMerge)
# 列表
listPublic = ['hua','hua','de']
listPublicTwo = ['bei','bei']
listPublicMerge = listPublic + listPublicTwo
print(listPublicMerge)
# 元组
tuplePublic = (1,2,3)
tuplePublicTwo = (4,5)
tuplePublicMerge = tuplePublic + tuplePublicTwo
print(tuplePublicMerge)

# *：复制——字符、列表、元组：乘以倍数
strPublicCopy = strPublic * 4
print(strPublicCopy)
listPublicCopy = listPublic * 3
print(listPublicCopy)
tuplePublicCopy = tuplePublic * 1
print(tuplePublicCopy)

# 判断是的否存在——in、not in——字符、列表、元组、字典
print('a' in 'abc')
print('hua' in listPublic)
print('hua' in tuplePublic)
print('hua' not in tuplePublic)
"""
# 公共操作
"""
# 计算容器元素个数
str1 = 'qwert'
print(len(str1))
# 删除容器
'''
del str1
print(str1)
list1 = [1,2]
del list1
print(list1)
'''
# 取容器中最大值
str2 = 'abcdefg'
list2 = [1,2,3,4]
print(max(str2))
print(max(list2))
# 取容器中最小值
print(min(list2))
print(min(str2))
# ⽣生成从start到end的数字，步⻓长为 step，供for循环使⽤用。可创建一个整数列表，然后用for循环取出
for i in range(2):
    print(i)
for j in range(1,10,2):
    print(j)
# 遍历获取函数
for q in enumerate(list2,start=2):
    print(q)
for index,char in enumerate(list2):
    print(index,char)
"""
# 数据类型转换函数
# 转换成元组
list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 300, 400, 500}
print(tuple(list1))
print(tuple(s1))
# 转换成列表
t1 = ('a', 'b', 'c', 'd', 'e')
s1 = {100, 200, 300, 400, 500}
print(list(t1))
print(list(s1))
# 转换成集合
list1 = [10, 20, 30, 40, 50, 20]
t1 = ('a', 'b', 'c', 'd', 'e')
print(set(list1))
print(set(t1))