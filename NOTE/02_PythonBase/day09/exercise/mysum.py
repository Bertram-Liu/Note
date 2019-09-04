# 练习:
#   写一个函数,mysum可以传入任意个实参的数字,返回所有实参的和
#   如:
#     def mysum(*args):
#         ...
#     print(mysum(1, 2, 3, 4))  # 10
#     print(mysum(100, 200, 300)) # 600


# 方法1
# def mysum(*args):
#     s = 0
#     for x in args:
#         s += x
#     return s

# 方法2
def mysum(*args):
    s = 0  # 累加和
    i = 0  # i代表索引
    while i < len(args):
        s += args[i]
        i += 1
    return s

print(mysum(1, 2, 3, 4))  # 10
print(mysum(100, 200, 300)) # 600
