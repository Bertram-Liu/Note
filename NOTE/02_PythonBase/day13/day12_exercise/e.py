#   3. 编写函数fun(n) 返回下列多项式的和
#      Sn = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
#      求n 为10时,Sn的值


# 方法1
# def fun(n):
#     import math
#     sn = 0
#     for x in range(n + 1):
#         sn += 1 / math.factorial(x)
#     return sn

# 方法2
def fun(n):
    import math
    # return sum([1/math.factorial(x) for x in range(n+1)])
    return sum(map(lambda x: 1 / math.factorial(x),
                   range(n + 1)))

print(fun(10))
print(fun(20))

