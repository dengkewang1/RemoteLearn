'''
# 第一步：print('1 * 1 =',1 * 1)
# 第二步
a = 1
while a <= 9:
    print(f'{a} * 1 = {a * 1}')
    a += 1
# 第三步
a = 1
while a <= 9:
    b = 1
    while b <= 9:
        print(f'{a} * {b} = {a * b}')
        b += 1
    a += 1
# 第四步
# a = 1
# while a <= 9:
#     b = 1
#     while b <= a:
#         # print('第一行shart')
#         print(f'{a} * {b} = {a * b}')
#         b += 1
#     print('第一行end')
#     a += 1
'''
# 第五步
a = 1
while a <= 9:
    b = 1
    while b <= a:
        # print('第一行shart')
        print(f'{a} * {b} = {a * b}',end='')#这里添加end=''或者end='\t'，是因为print()函数自带换号，如同步骤四中不添加换号的结果
        b += 1
    print('第一行end')
    a += 1
