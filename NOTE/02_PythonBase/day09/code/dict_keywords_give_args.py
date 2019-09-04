
# 此示例示意函数的字典关键字传参
def myfun1(a, b, c):
    print('a绑定的是:', a)
    print('b绑定的是:', b)
    print('c绑定的是:', c)

d1 = {"c": 33, "b": 22, "a": 11}
# myfun1(c=d1['c'], b=d1['b'], a=d1['a'])
myfun1(**d1) # 等同于上述函数调用

d2 = {"c": 33, "b": 22, "a": 11}
myfun1(**d2)





