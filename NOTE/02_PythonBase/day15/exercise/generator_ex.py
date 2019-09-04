# 练习:
#   1. 已知有列表:
#     L = [2, 3, 5, 7]
#     1) 写一个生成器函数,让此函数能够动态的提供数据,数据为原
#        列表的数字的平方加1
#     2) 写一个生成器表达式,让此表达式能够动态提供数据,数据为原
#        列表的数字的平方加1
#     3) 生成一个列表,此列表的数据为原列表的数字的平方加1
  



L = [2, 3, 5, 7]
# 1) 写一个生成器函数,让此函数能够动态的提供数据,数据为原
#     列表的数字的平方加1
def mypow(lst):
    for x in lst:
        yield x ** 2 + 1
# 测试代码:
for x in mypow(L):
    print(x)  # 5 10 26 50

print('--------------------')
# 2) 写一个生成器表达式,让此表达式能够动态提供数据,数据为原
#     列表的数字的平方加1
gen = (x ** 2 + 1 for x in L)
for y in gen:
    print(y)

print('====================')
# 3) 生成一个列表,此列表的数据为原列表的数字的平方加1
L2 = [x ** 2 +1 for x in L]
print(L2)

  
