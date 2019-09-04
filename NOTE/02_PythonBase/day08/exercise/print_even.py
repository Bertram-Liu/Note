# 练习:
#   写一个函数print_even, 传入一个参数n,代表终止的整数
#   打印 0 2 4 6 8 ... n 以内的所有偶数,打印在一行内
#   函数定义如下:
#     def print_even(n):
#         ...
#     # 测试调用:
#       print_even(10)  # 打印 0 2 4 6 8 10

    
def print_even(n):
    for x in range(0, n + 1, 2):
        print(x, end=' ')
    print()  # 换行



print_even(10)  # 打印 0 2 4 6 8 10
print_even(20)

    