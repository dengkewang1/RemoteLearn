import time
# 格式化输出：主要牢记%s、%d、%f
strName = '王登科'
date1 = time.ctime()
str2 = '体检'
str3 = '身高'
out1 = 169.5
print('%s%s%s%s%.2f'% (strName,date1,str2,str3,out1))# %f 格式化输出默认6位，所以为了保留两位小数为 %.2f
# f{'表达式'}
strName = '王登科'
date1 = time.ctime()
str2 = '体检'
str3 = '身高'
out1 = 169.5
print(f'{strName},{date1}{str2}{str3}{out1}')#f表达式格式化中不必添加‘，’号，以免以string格式输出
# 转义字符串\n、\t
print(strName)
print(str2)
print(strName,end='')#end结束符后不可添加输出没人，必然提示语法出错误，如：print(strName,end='',str2)
print(str2)
