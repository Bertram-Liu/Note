#   2. 已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数print_list(lst) 打印出所有的数据
#       print_list(L)  # 打印 3 5 8 10 13 14 ...
#       注: 不要求打印在一行内
#     2) 写一个函数sum_list(lst) 返回这个列表中所有数字的和
#        print(sum_list(L))  # 106
#       注:
#         type(x) 可以返回一个对象的类型
#         如:
#            >>> type(10) is int  # True
#            >>> type([3, 5, 8]) is list  # True



L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

def print_list(lst):
    for x in lst:
        if type(x) is int:  # 如果整数,则打印
            print(x)
        else:  # 如果是列表,则用prine_list来打印
            print_list(x)  # 递归调用

print_list(L)  # 打印 3 5 8 10 13 14 ...

def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is int:
            s += x
        else:
            s += sum_list(x)
    return s

print(sum_list(L))  # 106


