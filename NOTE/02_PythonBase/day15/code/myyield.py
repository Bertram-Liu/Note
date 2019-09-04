# myyield.py 

# 此示例示意生成器函数的定义和调用方式


def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3

    print('生成器函数调用结束')

g = myyield()  # g绑定的是一个生成器,生成器是可迭代对象
print("g绑定的是:", g)  # g=<generator object ...at >

it = iter(g)  # it 绑定g的迭代器
v = next(it)
print('v=', v)  # v=2
v2 = next(it)
print('v2=', v2)  # v2=3
v3 = next(it)  # 触发StopIteration异常
print('v3=', v3)   







