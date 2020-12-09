# 1.把上次课的作业重新编程（不能看着答案，把分析过程写出来再敲代码）
# 	99乘法表；质数判断；三角形打印；斐波那契数列
# 2.打印由*组成的菱形，该菱形一共7行，已在群里发了，大家自己找图
# 3.使用列表推导式生成能被5整除的数（100以内）
list1 = [i for i in range(1,101) if i%5 == 0]
print(list1)
# 4.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
list_name = ('Tom','Rose','Jack')
list_age = (15,16,17)
dict1 = {}
for i in range(len(list_name)):
    dict1[list_name[i]] = list_age[i]
    # dict1 = {list_name[i], list_age[i]}
print(dict1)
dict2 = {list_name[j]:list_age[j] for j in range(len(list_name))}
print(dict2)
# 5.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},xxx]
# ----------------
# *   1-新增用户
# *   2-查询用户
# *   3-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息