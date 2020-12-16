# 7.	有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转（15分）（只写了一半）
'''
str1 = 'welocme to super&Test'
str1_newlist = str1.split(' ', 2)
list9 = []
print(str1_newlist)
for newStr1 in str1_newlist:
    n2 = list(newStr1)
    i = len(newStr1) - 1
    j = 0
    while j <= i//2:
        n2[j], n2[i-j] = n2[i-j], n2[j]
        j += 1
    newN2 = ''.join(n2)
    list9.append(newN2)
print(list9)
'''
# 4.	文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
'''
lucy:21，tom:30
xiaoming:18，xiaohong:15
xiaowang:20，xiaohei:19
输出年龄大于18岁的人名
'''
f = open("E:/Learn-wdk/WorkSpace/PycharmProjects/untitled1/learnReviewFourDay/test.txt", encoding='utf-8')
content = f.readlines()
# print(content)
list1 = []
dist1 = {}
for a in content:
    # print(type(a))
    b = a.strip('\n')
    # print(type(b))
    # print(b)
    c = b.split('，')
    # print(c)
    for oldc in c:
        newc = oldc.split(':')
        # print(newc)
        dist1[newc[0]] = int(newc[1])
# for key, value in dist1.items():
#     if value > 18:
#         print(f'{key}')
count1 = {key: value for key, value in dist1.items() if value > 18}
print(count1)