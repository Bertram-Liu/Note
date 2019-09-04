#   1. 用filter函数生成 1~20之间的全部偶数(不包含20):
#     将这些数字存于列表中,再打印这个列表

L = list(filter(lambda x: x %2 == 0, range(1, 20)))

print(L)  # [2, 4, 6, 8 ...]
