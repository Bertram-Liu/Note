# 练习:
#   写一个函数,mysum可以传入任意个实参的数字,返回所有实参的和
#   如:
#     def mysum(*args):
#         ...
#     print(mysum(1, 2, 3, 4))  # 10
#     print(mysum(100, 200, 300)) # 600



def mysum(*args):
    s = sum(args)  # s=sum( (1,2,3,4) )
    # s = sum(*args)  # s = sum(1, 2, 3, 4) 错误
    return s

print(mysum(1, 2, 3, 4))  # 10


# print(mysum(100, 200, 300)) # 600
