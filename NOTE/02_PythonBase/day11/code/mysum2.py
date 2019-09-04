# 此示例示意用函数式编程的方式解决求和问题
def mysum(x):
    return sum(range(1, x + 1))

print(mysum(100))  # 5050
print(mysum(10))  # 55

# 求1 + 2 + 3 + ..... + 1000 的和
print(sum(range(1, 1001)))  # 函数式编程
