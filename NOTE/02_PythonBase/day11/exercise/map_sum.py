# 练习:
#   1. 求 1**2 + 2**2 + 3**2 + .... + 9**2 的和
#   2. 求 1**3 + 2**3 + 3**3 + .... + 9**3 的和
#   3. 求 1**9 + 2**8 + 3**7 + .... + 9**1 的和
  


# 1. 求 1**2 + 2**2 + 3**2 + .... + 9**2 的和
# 方法1
# s = 0
# for x in range(1, 10):
#     s += x ** 2
# print(s)

# 方法2
# s = 0
# for x in map(pow, range(1, 10), [2] * 9):
#     s += x
# print(s)

# 方法3
# def power2(x):
#     return x ** 2
# print(sum(map(power2, range(1, 10))))

# 方法4
print(sum(map(lambda x: x**2, range(1, 10))))

# 2. 求 1**3 + 2**3 + 3**3 + .... + 9**3 的和
print(sum(map(lambda x: x**3, range(1, 10))))

# 3. 求 1**9 + 2**8 + 3**7 + .... + 9**1 的和
print(sum(map(pow, range(1, 10), range(9, 0, -1))))

  
