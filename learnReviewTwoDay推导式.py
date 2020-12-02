# 推导式

# 列表推导式
"""
# 循环推导式
list1 = []
for i in range(11):
    list1.append(i)
print(list1)
list2 = [i for i in range(11)]
print(list2)
# 判断推导式
list3 = []
for a in range(11):
    if a%2 == 0:
        list3.append(a)
print(list3)
list4 = [a for a in range(11) if a%2 == 0]
print(list4)
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list5 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list1)

list_muster = []
for i in range(1,3):
    for j in range(3):
        tuple1 = (i,j)
        list_muster.append(tuple1)
print(list_muster)
"""
# 字典推导式
"""
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)

dict2 = dict()
for key1 in range(1,5):
    # dict2 = {key1:key1**2}
    dict2[key1] = key1 ** 2
print(dict2)

list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
listMuster = {list1[i]:list2[i] for i in range(len(list1))}
print(listMuster)

pc = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提取上述电脑数量量⼤大于等于200的字典数据
dictUp = {}
for pcKey,pcValue in pc.items():
    if pcValue >= 200:
        dictUp[pcKey] = pcValue
print(dictUp)
dictUp1 = {pcKey1 : pcValue1 for pcKey1,pcValue1 in pc.items() if pcValue1 >= 200}
print(dictUp1)
"""
# 集合推导式
"""
list1 = [1, 1, 2]
# list1的2次方
set1 = set()
for i in list1:
    j = i ** 2
    set1.add(j)
print(set1)

set2 = {i**2 for i in list1}
print(set2)
"""