# 元组

# 元组不可修改的变量类型
# 定义元组：定义多数据元组、定义但数据元组
tupleOne = (1,2,3)
tupleTwo = (4,)
print(tupleOne,tupleTwo)

# 元组查询
# 下标查询、取值
print(tupleOne[2])
# 根据index函数查询数据下标
print(tupleTwo.index(4))
# 查询重复个数
print(tupleOne.count(1))
# 获取元组的数据个数
print(len(tupleOne))
