# 练习:
#   写一个生成器函数 myeven(start, stop) 用来生成从start开始
#   到stop结束(不包含stop)区间内的一系列偶数
#   如:
#     def myeven(start, stop):
#         ...

#     events = list(myeven(10, 20))
#     print(events)  #  [10, 12, 14, 16, 18]
#     for x in myeven(21, 30):
#         print(x)  # 打印: 22 24 26 28
#     L = [x**2 for x in myeven(1, 10)]
#     print(L)  # [4, 16, 36, 64]


# def myeven(start, stop):
#     # i = start
#     if start % 2 == 1:
#         start += 1
#     while start < stop:
#         yield start
#         start += 2

def myeven(start, stop):
    while start < stop:
        if start % 2 == 0:
            yield start
        start += 1

events = list(myeven(10, 20))
print(events)  #  [10, 12, 14, 16, 18]
for x in myeven(21, 30):
    print(x)  # 打印: 22 24 26 28
L = [x**2 for x in myeven(1, 10)]
print(L)  # [4, 16, 36, 64]

for x in myeven(23, 24):
    print(x)


