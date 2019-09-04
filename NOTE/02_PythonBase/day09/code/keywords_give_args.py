
# 此示例示意函数的关键字传参
def myfun1(a, b, c):
    print('a绑定的是:', a)
    print('b绑定的是:', b)
    print('c绑定的是:', c)

myfun1(a=11, c=33, b=22)   # 11->a  22->b  33->c   myfun1(11,22,33)
myfun1(c=300, b=200, a=100)






