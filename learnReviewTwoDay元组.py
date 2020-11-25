# 元组的定义:使⽤用⼩小括号，且逗号隔开
one_tuple = (11,22,33)
# 定义只有一个数据的tuple
onlyone_tuple = (1,)

# 元组不支持修改，只能查询
# 查询
# 下标查询
print(one_tuple[0])
# 函数查询
# index
print(one_tuple.index(22))
# count
print(one_tuple.count(11))
# len()
print(len(one_tuple))

# 元组中存在列表查询
tuple2 = (10, 20, ['aa', 'bb', 'cc'], 50, 30)
print(tuple2[2][2])