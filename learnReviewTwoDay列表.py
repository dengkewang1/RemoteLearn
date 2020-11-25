# 列表：增删改查
# 查询
"""
# 下标查询
namelist = ['zhangsan','lisi','lisi','wangwu']
print(namelist[2])
# 函数查询
# index查询：查询数据所在位置
print(namelist.index('lisi'))
# print(namelist.index('lisi',0,1))#ValueError: 'lisi' is not in list
# count查询：查询数据在列表里的个数
print(namelist.count('lisi'))
print(namelist.count('lisi'))
# 获取列表的长度
print(len(namelist))
# 查询判断(true false)：in、not in
print('lisi' in namelist)
print('zhoaliu' in namelist)
print('zhaoliu' not in namelist)
"""
#增加
"""
# 追加增加：append——列表.append('数据')
namelist = ['zhangsan','lisi','lisi','wangwu']
namelist.append(['zhaoliu'])
print(namelist)
#延伸追加（列表尾部追加）：extend——；列表.extend('数据')
namelist.extend('leilie')
print(namelist)
# 指定位置插入：insert——列表.insert(下标,数据)
namelist.insert(2,'momo')
print(namelist)
"""
# 删除:
"""
# 删除：del——del 目标
#删除列表
namelist = ['zhangsan','lisi','lisi','wangwu']
'''
del namelist
print(namelist)
'''

# 删除列表中指定数据
'''
del namelist[1]
print(namelist)
'''
# 删除pop——列表.pop(下标)
'''
namelist.pop(2)
print(namelist)
'''
# pop可返回删除内容
'''
pop_name = namelist.pop(2)
print(pop_name)
'''
# 移除remove——列表.remove(数据)
namelist.remove('lisi')
print(namelist)
# 清空列表clear——列表.clear()
namelist.clear()
print(namelist)
"""
# 改
namelist = ['zhangsan','lisi','lisi','wangwu']
"""
# 指定下标修改——列表[下标] = 数据
'''
namelist[1] = 'xmx'
print(namelist)
'''
# 逆置 reverse()
namelist.reverse()
print(namelist)
# 排序 sort
num_list = [1,2,3,7,5]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
# 复制
num_list1 = num_list.copy()
print(num_list1)
"""
# 列表嵌套
'''
name_list = [['⼩小明', '⼩小红', '⼩小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李李四','王五']]
print(name_list[1][1])
'''
# 列表循环
# whil循环
name_list = ['Tom', 'Lily', 'Rose']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
# for循环
for i in name_list:
    print(i)