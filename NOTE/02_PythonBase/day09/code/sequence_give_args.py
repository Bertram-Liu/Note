
# 此示例示意函数的位置传参中的序列传参
def myfun1(a, b, c):
    print('a绑定的是:', a)
    print('b绑定的是:', b)
    print('c绑定的是:', c)


S1 = [11, 22, 33]
S2 = (44, 55, 66)
S3 = "ABC"
# myfun1(S1[0], S1[1], S1[2])
myfun1(*S1)
myfun1(*S2)
myfun1(*S3)









