# 练习:
#   已知内建函数max的帮助文档为:
#     max(...)
#       max(iterable)
#       max(arg1, arg2, *args)
#     仿造max 写一个mymax函数,功能与max完全相同
#     (要求: 不允许调用max函数)
#     如:
#       def mymax(...):
#           ...
#       print(mymax([6, 8, 3, 5]))  # 8
#       print(mymax(100, 200))  # 200
#       print(mymax(1, 3, 5, 9, 7))  # 9




def mymax(a, *args):
    if not args:  # 当args绑定空元组时,a绑定可迭代对象
        return max(a)
    else:  # 当mymax传入两个或两个以上实参时
        # return max(args + (a,))
        return max(a, *args)


print(mymax([6, 8, 3, 5]))  # 8
print(mymax(100, 200))  # 200
print(mymax(1, 3, 5, 9, 7))  # 9
