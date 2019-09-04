# 此示例示意用递归求阶乘

# 5! = 5 * 4!
# 5! = 5 * 4 * 3!
# 5! = 5 * 4 * 3 * 2!
# 5! = 5 * 4 * 3 * 2 * 1!
# 5! = 5 * 4 * 3 * 2 * 1 * 0!
# 5! = 5 * 4 * 3 * 2 * 1 * 1
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120


def myfac(n):
    if n == 0:
        return 1
    r = n * myfac(n-1)
    return r

print(myfac(0))  # 1

print(myfac(5))  # 120
print(myfac(6))  # 720

