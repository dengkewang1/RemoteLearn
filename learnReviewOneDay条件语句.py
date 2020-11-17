# clientAge = int(input('请输入您的年龄：'))
# if clientAge >= 18:
#     print('您已成年，可以上网')
# print('系统关闭')
"""
# if else
clientAge = int(input('请输入您的年龄：'))
if clientAge >= 18:
    print('您已成年，可以上网')
else:
    print('你未成年，不可以上网')
if elif else
clientAge = int(input('请输入您的年龄：'))
if clientAge < 18:
    print('未成年')
elif  18 <= clientAge <= 60:
    print('成年人')
else:
    print('老年人')
"""
'''
money = int(input('您是否有钱：'))
# 0为是，1为否
if money == 0:
    print('请上车1')
    seat = int(input('是否有座'))
    if seat == 0:
        print('未了您的安全请入座！')
    else:
        print('请抓紧扶手！')
else:
    print('请充值后刷卡上车！')
'''
"""
# 剪发 0，石头 1，布 2
import random
PC = random.randint(0,2)
client = int(input('剪刀、石头、布:'))
if ((client == 0) and (PC == 1) or (client == 1) and (PC == 2) or (client == 2) and (PC == 0)):
    print('PC胜利')
elif client == PC:
    print('平局')
else:
    print('client胜利')
print(client,PC)
"""
a = 1
b = 2
c = a if a < b else b
print(c)