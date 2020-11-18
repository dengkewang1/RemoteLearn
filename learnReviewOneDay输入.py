# 输入的语法
# input('提示信息')
userName = input('请输入的名字：')
passWord = input('请输入你的密码：')
passWordTwo = input('请再次输入您的密码：')

if passWordTwo == passWord:
    print('登录成功')
    print(type(passWordTwo)) #input() 接收的数据默认为字符串
else:
    print('登录失败')
    print(type(passWordTwo))