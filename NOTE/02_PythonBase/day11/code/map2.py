# map2.py

# 生成一个可迭代对象,此可迭代对象可以生成如下数字
#   1**4   2**3   3**2  4**1
#     1      8      9    4
for x in map(pow, range(1, 10), range(4, 0, -1)):
    print(x)


print('-------------')
for x in map(pow, range(1, 10),
                  range(4, 0, -1),
                  range(5, 10)
            ):
    print(x)



