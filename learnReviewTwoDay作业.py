# 2、求100以内能被3整除的数，并将作为列表输出
"""
list = []
for i in range(100):
    if i % 3 == 0:
        list.append(i)
print(list)
"""
# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
"""
list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
list12 = []
a = len(list1)
b = 0
while b < a:
    out = list1[b]
    if out in list12:
        b += 1
        continue
    else:
        list12.append(out)
        b += 1
print(list12)
"""
# 求斐波那契数列 1 1 2 3 5 8 13 ……
"""
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""



# n == 4
# def demo(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return demo(n - 1) + demo(n - 2)
# print(demo(7))

# 5、求100以内的质数（只能被1和它本身整除）
"""
list1 = []
for z in range(2,101):
    for z1 in range(2,z):
        if z % z1 == 0:
            break
    else:
        list1.append(z)
print(list1)
"""
# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
"""
str1 = 'aabbbcddef'
list1 = []
for n in str1:
    if str1.count(n) == 1:
        print(n,end='')
#         list1.append(n)
# print(list1)
"""
# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
str8 = 'welocme to super&Test'
str81 = list(str8)
str81.reverse()
print(''.join(str81))
# 9、有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
"""
str9 = 'abcdef'
list9 = []
j = len(str9) - 1
while j >= 0:
    list9.append(str9[j])
    j -= 1
    str91 = ''.join(list9)
print(str91)
"""
# 10、有一堆字符串，“aabbbcddef”，输出abcdef
"""
str10 = 'aabbbcddef'
str11 = ''
for i in range(len(str10)):
    if str10[i] not in str11:
        str11 = str10[i]
        print(str11,end='')
"""
