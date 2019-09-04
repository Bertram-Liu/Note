# filter.py

# 此示例示意filter函数的使用

def is_odd(x):
    '''判断x是否是奇数,如果是奇数返回True,否则返回False'''
    return x % 2 == 1

# 生成从 0 到 20 以内的奇数:
for x in filter(is_odd, range(0, 20)):
    print(x)

# 创建一个列表,此列表内的数据为1~100之间的奇数 
L = [x for x in filter(is_odd, range(1, 100))]
print(L)


