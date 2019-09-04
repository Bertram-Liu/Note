#   3. 写一个函数myfun(n) 计算:
#      1 + 2**2 + 3**3 + ... + n**n的和
#     如:
#       print(myfun(3))  # 32

# 方法1
# def myfun(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += i ** i
#     return s

# 方法2
def myfun(n):
    return sum(map(lambda x: x**x, range(1, n+1)))

print(myfun(3))  # 32