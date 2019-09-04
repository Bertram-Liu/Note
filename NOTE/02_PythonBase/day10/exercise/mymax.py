#   2. 写一个lambda 表达式来创建函数,此函数返回两个形参的最大值
#     如:
#       def mymax(x, y):
#           ...
#     改写后
#       mymax = lambda .....
#     测试代码:
#       print(mymax(100, 200))  # 200



def mymax(x, y):
    return x if x > y else y



# 改写后
# mymax = lambda x, y: x if x > y else y
mymax = lambda x, y: max(x, y)

# 测试代码:
print(mymax(100, 200))  # 200



