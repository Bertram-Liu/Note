#   1. 写一个函数mysum(x) 来计算
#     1 + 2 + 3 + 4 + .... + x 的和
#     要求: 不允许调用sum函数
#     如:
#        print(mysum(100))  # 5050

def mysum(x):
    s = 0
    for i in range(1, x + 1):
        s += i
    return s

print(mysum(100))  # 5050
print(mysum(10))  # 55