#   1. 写一个函数 mymax.实现返回两个数的最大值
#     如:
#       def mymax(a, b):
#           ...
#       print(mymax(100, 200))  # 200
#       print(mymax("ABC", "123"))  # ABC


# def mymax(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)


# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b


# def mymax(a, b):
#     if a > b:
#         return a
#     return b

def mymax(a, b):
    return max(a, b)


print(mymax(100, 200))  # 200
print(mymax("ABC", "123"))  # ABC
