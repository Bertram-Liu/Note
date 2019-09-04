#   3. 写一个生成器函数myxrange([start, ] stop[, step]) 来
#      生成一系列整数,
#        要求:
#           myxrange功能与range功能完全相同
#           不允许调用range函数和列表

def myxrange(start, stop=None, step=None):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1

    # 正向
    if step > 0:
        while start < stop:
            yield start
            start += step
    # 反向
    else:
        while start > stop:
            yield start
            start += step  # 加上负的步长

for x in myxrange(3):
    print(x)

for x in myxrange(100, 103):
    print(x)

for x in myxrange(1000, 1010, 3):
    print(x)

for x in myxrange(10, 0, -3):
    print(x)

