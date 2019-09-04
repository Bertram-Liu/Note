#   4. 写一个函数myrange,可以传入1~3个参数,实际意义与range函
#     数完全相同,返回符合range函数规则的列表
#     如:
#       L = myrange(4)
#       print(L)  # [0, 1, 2, 3]
#       L = myrange(4, 6)
#       print(L)  # [4, 5]
#       L = myrange(1, 10, 3)
#       print(L)  # [1, 4, 7]
#       (可以调用range函数)


def myrange(a, b=None, c=None):
    if b is None:
        start = 0  # 开始值
        stop = a   # 结束值
    else:
        start = a
        stop = b 
    # 重新确定步长
    if c is None:  # 没有给第三个参数
        step = 1  #步长
    else:
        step = c

    L = []  # 先创建列表
    # 此处添加附合条件的数据
    for x in range(start, stop, step):
        L.append(x)

    return L


L = myrange(4)
print(L)  # [0, 1, 2, 3]
L = myrange(4, 6)
print(L)  # [4, 5]
L = myrange(1, 10, 3)
print(L)  # [1, 4, 7]

