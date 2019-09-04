#   1. 写程序算出1~20的阶乘的和
#     即:
#       1! + 2! + 3! + ... + 19! + 20!

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# 方法1
s = 0
for x in range(1, 21):
    s += factorial(x)

print(s)

# 方法2
print(sum(map(factorial, range(1, 21))))

