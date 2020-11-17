# 算数运算符
a = 1
b = 2
c = 3
d = 4
print('计算：%d' % (d - a + 1 * b / 1))
print(c / d)
print(c // d)
print(d % c)
# 赋值
# 单变量赋值
num1 = 1
# 多变量赋值
num2,num3,num4 = 2,3,4
print(num1,num2,num3,num4)
#多变量同一值赋值
number1 = number2 = number3 = 10
print(f'{number1},{number2},{number3}')
# 符合运算符
a11 = 1
a11 += 1
print(a11)
# 比较运算符
a111 = 7
b111 = 5
print(a111 == b111)
print(a111 != b111)
print(a111 < b111)
# 逻辑运算符
print(end='\n')
print((a < b) and (b < d))#全真
print((a > b) and (b > d))#全假
print((a < b) and (b > d))#先真 后假
print((a > b) and (b < d))#先假 后真
print(end='\n')
print((a < b) or (b < d))#全真
print((a > b) or (b > d))#全假
print((a < b) or (b > d))#先真 后假
print((a > b) or (b < d))#先假 后真
print(end= '\n')
print(not(a < b))#非真为假
print(not(a > b))#非假为真