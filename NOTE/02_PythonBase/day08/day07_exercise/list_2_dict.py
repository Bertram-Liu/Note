#   2. 已知有两个等长度的列表:
#      list1 = [1001, 1003, 1008, 1006]
#      list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
#     生成如下字典:
#       {'Tom': 1001, 'Jerry': 1003, 'Spike': 1008,
#         'Tyke': 1006}


list1 = [1001, 1003, 1008, 1006]
list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']

# 方法１，用循环实现
# d = {}
# for i in range(len(list1)):
#     d[list2[i]] = list1[i]

# 方法2
# d = {list2[i]: list1[i] for i in range(len(list1))}

# 方法3
d = {}
for x in list1:
    i = list1.index(x)  # i代表索引
    k = list2[i]  # 键
    d[k] = x


print(d)


#   {'Tom': 1001, 'Jerry': 1003, 'Spike': 1008,
#     'Tyke': 1006}
