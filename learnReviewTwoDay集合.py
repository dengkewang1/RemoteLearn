# set集合：为可变类型、无下标、去重

# 定义：定义空的集合、定义有数据的集合
setOne = set()
setTwo = {1,2,3,4,'name'}
print(setOne)
print(setTwo)

# 增
# 追加数据
setTwo.add('age')
print(setTwo)
#追加序列
setTwo.update('birthday')#如列表中的extend
print(setTwo)
setTwo.update(['birthday'])
print(setTwo)

# 删除
# 移除
setTwo.remove('birthday')
print(setTwo)
# setTwo.remove('birthday')#移除内容不存在报错：KeyError: 'birthday'
# 删除指定数据
setTwo.discard('age')
print(setTwo)
setTwo.discard('age')#不存也不会报错
print(setTwo)
# 随机删除
setTwo.pop()
print(setTwo)

# 查询
# 在
print(2 in setTwo)
# 不在
print(1 not in setTwo)