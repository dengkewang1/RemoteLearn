# 创建字符串
"""
name1 = 'Tom'
age1 = '18'
print(type(name1),type(age1))
p = "1'm Rose,nice to meet you"
print(p)
p1 = '''1'm Rose,
     nice to meet you'''
print(p1)
# 转移
p3 = '1\'m Rose,nice to meet you'
print(p3)
"""
# 体验字符串的下标
# name = 'qwertwer'
'''
print(name[1])
print(name[0])
'''
# 切片：字符串序列【开始下标：结束下标：步长】
'''
print(name[2:6:2])
print(name[::2])
print(name[:-1])
print(name[2::-2])
'''
# 查找：字符串序列.find(子串，开始位置下标，结束为止下标)
'''
a = name.find('w')
b = name.find('w',a + 1,)
print(a,b)
'''
 # 最后解决
'''
a = 0
set1 = set()
while a <= len(name):
    b = name.find('w',a + 1,)
    a += 1
    if b > 0:
        set1.add(b)
        print(set1)
else:
    print('end')
'''
'''
findReturError = name.find('c')
print(findReturError)
'''
# 查找：字符串序列.index(子串，开始位置下标，结束为止下标)
mystr = "hello world and supertest and chaoge and Python"
'''
mystrIndex = mystr.index('and')
mystrIndex1 = mystr.index('and',15,40)
print(mystrIndex,mystrIndex1)
mystrIndex2 = mystr.index('ands')
print(mystrIndex2)
'''
'''
mystr_find_right = mystr.find('and')
mystr_index_right = mystr.index('and')
print(mystr_find_right,mystr_index_right)
'''
# 查询子字符串在字符串序列中的个数---字符串序列.count('子串'，开始位置下标，结束位置下标)
"""
mystr_count_out = mystr.count('and')
print(mystr_count_out)
"""
# 将新的子字符串替换指定旧的字符串---字符串序列.replace(旧子串，新子串，替换次数)
"""
print(mystr)
mystr_replace_out = mystr.replace('and','or')
print(f'{mystr_replace_out}---{mystr}')#str字符串是不可变类型
mystr_replace_out1 = mystr.replace('and','he',1)
print(mystr_replace_out1)
"""
# 分割字符串：mystr.split(分割字符，num)
"""
mystr_split_out = mystr.split('and')
mystr_split_out1  = mystr.split('and',2)
print(mystr)
print(mystr_split_out)
print(mystr_split_out1)#分割字符串后变为列表
print(f'{type(mystr)}--{type(mystr_split_out)}')
"""
# 合并连接字符串（或者将list列表转成str字符串）：字符串或者子串.join(多个字符串组成的序列)
"""
list1 = ['chao', 'ge', 'test', 'promotion']
t1 = ('aa', 'b', 'cc', 'ddd')
print(type(list1),type(t1))
list1_to_str = (',').join(list1)
tuple_to_str = ('_').join(t1)
print(list1_to_str,type(list1_to_str))
print(tuple_to_str,type(tuple_to_str))
str_to_str = ('--').join(mystr)
print(str_to_str)
"""
#字符串序列.capitalize()---将字符串首字母大写
# 字符串序列.titel()---将字符串中每个单词首字母大写
# 字符串序列.lower()---将字符串中大写改为小写
#字符串序列.upper()---将字符窜中小写改为大写
"""
mystr_capitaleze_out = mystr.capitalize()
mystr_title_out = mystr.title()
mystr_upper_out = mystr.upper()
mystr_lower_out = mystr_upper_out.lower()
print(mystr_capitaleze_out)
print(mystr_title_out)
print(mystr_upper_out)
print(mystr_lower_out)
"""
# 删除空格:左、右、两侧都删除
# lstrip()
# rstrip()
# strip(）
"""
mystr1 = "   hello world and supertest and chaoge and Python    "
mystr1_lstrip_out = mystr1.lstrip()
mystr1_rstrip_out = mystr1.rstrip()
mystr1_strip_out = mystr1.strip()
print(mystr1_lstrip_out)
print(mystr1_rstrip_out)
print(mystr1_strip_out)
"""
# 居中、左对齐、右对齐-------输出问题
"""
mystr3 = 'hello world'
print(mystr3.center(3,'.'))
print(mystr3.ljust(3,'_'))
print(mystr3.rjust(3,'*'))
"""

a = 'mn'
b = 'qw'
c = a.join(b)
print(c)

mystr = "hello world and supertest and chaoge and Python"
mystr2 = mystr.upper()
print(mystr2)