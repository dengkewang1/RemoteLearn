# 字符串
"""
mystr = 'hello word'
# 下标查询
mystrOne = mystr[1]
print(mystrOne)
# 查询位置分为：find、index
mystrFind = mystr.find('l')
print(mystrFind)
mystrIndex = mystr.index('w')
print(mystrIndex)
# 查重：count
mystrCount = mystr.count('l')
print(mystrCount)

# 修改：字符串为不可变了类型
mystrMod = "hello world and supertest and chaoge and Python"
# 替换
mystrReplace = mystrMod.replace('and','or')
print(mystrReplace)
# 分割
mystrSplit = mystrMod.split('and',1)
print(mystrSplit)
mystrSplitNum = mystrMod.split(' ')
print(mystrSplitNum)
# 连接、合并
mystrJoin = '_'.join(mystrMod)
print(mystrJoin)
mystrSmart = 'smart'
mystrSmart_MystrMOd = mystrSmart.join(mystrMod)
print(mystrSmart_MystrMOd)

# 大小写
# 首字母大小写
mystrModCap  = mystrMod.capitalize()
print(mystrModCap)
# 字符串中的单词首字母大写
mystrMod_title = mystrMod.title()
print(mystrMod_title)
# 将字符串中的大写变为小写
mystrModCap_Lower = mystrModCap.lower()
print(mystrModCap_Lower)
# 将字符串中的小写变为大写
mystrModCap_Lower_upper = mystrModCap_Lower.upper()
print(mystrModCap_Lower_upper)

# 删除空白
# 删除两侧空白
mystrTwo = ' zhanglin '
mystrTwo_Strip = mystrTwo.strip()
print(mystrTwo_Strip)
# 删除左侧空白
mystrTwo_Left = mystrTwo.lstrip()
print(mystrTwo_Left)
# 删除右侧空白
mystrTwo_Right = mystrTwo.rstrip()
print(mystrTwo_Right)

# 对齐
# 居中对齐
mystrjust = 'hello'
print(mystrjust.center(10,'_'))
# 左对齐
mystrjust_left = mystrjust.ljust(10,'_')
print(mystrjust_left)
# 右对齐
mystrjust_right = mystrjust.rjust(10,'_')
print(mystrjust_right)

# 判断
# 从左开始是否存在
mystrMod_startswith = mystrMod.startswith('hello')
print(mystrMod_startswith)
mystrMod_startswithtwo = mystrMod.startswith('hello',9,15)
print(mystrMod_startswithtwo)
# 从尾部开始是否存在
mystrMod_enswith = mystrMod.endswith('hello',2,10)
# 判断是否包含数字、字母
mystrModnum = 'qwe123'
mystrModlitte = 'qwe'
mystrModnumber = '123'
print(mystrModnum.isalnum())
print(mystrModnumber.isdigit())
print(mystrModlitte.isalpha())
# 判断是否自包含空白
mystrtal = ' '
print(mystrtal.isspace())
"""
# 列表
"""
# 查询
# 下标查询
mylist = ['Tom', 'Lily', 'Rose']
print(mylist[2])
# 查询位置
mylist_index = mylist.index('Tom')
print(mylist_index)
# 查询重复
mylist_count = mylist.count('Tom')
print(mylist_count)

# 增加
# 将追加的序列整个加入
mylist.append('Lily')
print(mylist)
mylist.append(['Lily','zhangsan'])
print(mylist)
# 将追加的序列逐一加入
mylist.extend('Lily')
print(mylist)
mylist.extend(['Lily'])
print(mylist)
mylist.insert(3,'lisi')
print(mylist)

# 删除
# 删除列表
'''
del mylist
print(mylist)
'''
# 根据下标删除指定数据
del mylist[3]
print(mylist)
# 能返回所删除的数值
mylist.pop()#不输入下标，删除最后一个
print(mylist)
mylist_pop = mylist.pop(4)#将删除的数据赋值给一个变量
print(mylist)
print(mylist_pop)#打印出删除的数据
# 移除
mylist.remove('Lily')
print(mylist)
# 清空
mylist.clear()
print(mylist)

# 修改
# 指定下标修改
mylistone = [1,2,3,4]
mylistone[2] = 5
print(mylistone)
# 逆置
mylistone.reverse()
print(mylistone)
# 排序
mylistone.sort()
print(mylistone)
mylistone.sort(reverse=True)
print(mylistone)
# 复制
mylistone_copy = mylistone.copy()
print(mylistone_copy)

# 循环遍历
name_list = ['Tom', 'Lily', 'Rose']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
print()
for n in name_list:
    print(n)

# 列表嵌套（列表里有字列表）
# 获取列表里的字列表
name_list = [['⼩小明', '⼩小红', '⼩小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李李四','王五']]
print(name_list[2][1])
"""