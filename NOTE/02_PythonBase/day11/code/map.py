# map.py

def power2(x):
    print("power2传入:", x, '返回:', x**2)
    return x ** 2

# 生成一个可迭代对象,此可迭代对象可以生成1~9的平方
for x in map(power2, range(1, 10)): # 可迭代对象:
    print(x)  # 1, 4, 9, 16, ....

