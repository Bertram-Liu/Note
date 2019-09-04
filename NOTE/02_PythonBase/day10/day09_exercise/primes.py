#   1. 写一个函数 isprime(x) 判断x是否是素数,如果是素数返回
#      True,否则返回False
#   2. 写一个函数 prime_m2n(m, n) 返回从m开始,到n结束(不包含n)
#      范围内的素数的列表,并打印这些整数
#     如:
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]
#   3. 写一个函数primes(n) 返回指定范围n以内(不包含n)的素数的
#      列表,并打印
#     如: 
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#     1) 打印100以内的全部素数
#     2) 打印200以内全部素数的和


#   1. 写一个函数 isprime(x) 判断x是否是素数,如果是素数返回
#      True,否则返回False
def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

#   2. 写一个函数 prime_m2n(m, n) 返回从m开始,到n结束(不包含n)
#      范围内的素数的列表,并打印这些整数
def prime_m2n(m, n):
    L = []  # 先创建一个容器,准备存放[m, n),的素数
    for x in range(m, n):
        if isprime(x):
            L.append(x)
    return L

L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]

#   3. 写一个函数primes(n) 返回指定范围n以内(不包含n)的素数的
#      列表,并打印
def primes(n):
    return prime_m2n(0, n)

L = primes(10)
print(L)  # [2, 3, 5, 7]

# 1) 打印100以内的全部素数
print(primes(100))
# 2) 打印200以内全部素数的和
print(sum(primes(200)))
