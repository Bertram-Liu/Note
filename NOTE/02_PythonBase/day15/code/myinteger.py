# myinteger.py


# 写一个生成器函数myinteger(n), 此生成器函数可以生成
# 从零开始的一系列整数,到n结束(不包含n)

def myinteger(n):
    i = 0
    while i < n:
        yield i
        i += 1

L = []
for x in myinteger(30000000000000000):
    # print(x)  # 打印 0, 1, 2
    L.append(x)

# it = iter(myinteger(300000000000000000000000000000))
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break