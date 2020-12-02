# 字典dict：为可变类型、无下标

# 字典的定义：空字典、数据字典
dictOne = {}
dictTwo = {'name':'Tom','age':'18','sex':'男'}
print(dictTwo)

# 增：修改、增加——根据key修改对应的value，如果key不存在则新增此键值对
dictTwo['name'] = 'Rose'
print(dictTwo)
dictTwo['birthday'] = '2020-01-01'
print(dictTwo)

# 删除：删除字典、删除键值对，清空字典
del dictOne
del dictTwo['birthday']
# print(dictOne)
print(dictTwo)
# dictTwo.clear()
# print(dictTwo)

# 查
# 更具key查询
print(dictTwo['name'])
# print(dictTwo['birthday'])#不存在时报错：KeyError: 'birthday'
# 如果不存在则返回默认值，get(key,默认值)
print(dictTwo.get('birthday','2008-11-11'))
# 查询字典中所有的key
print(dictTwo.keys())
# 查询字典中所有的value
print(dictTwo.values())
# 查询字典
print(dictTwo.items())

# 遍历
# key的遍历
for keyOne in dictTwo.keys():
    print(keyOne)
# value的遍历
for valueOne in dictTwo.values():
    print(valueOne)
# 键值对的遍历
for keyTwo,valueTwo in dictTwo.items():
    print(keyTwo,valueTwo)