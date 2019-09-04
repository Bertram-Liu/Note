# mymod.py


# 此示例示意自定义模块的编码方法
''' 这是自定义模块mymod的标题

此模块有两个函数和两个数据
... 此处省略200字
'''


def myfac(n):
    print("正在求%d的阶乘!!!" % n)

def mysum(n):
    print("正在计算%d的和" % n)

name1 = "audi"

name2 = "tesla"

print('mymod模块已成功加载')

print('当前模块的模块名为:', __name__)
# 当mymod不是主模块时: __name__ = 'mymod'
# 当mymod 是主模块时: __name__ = '__main__'

if __name__ == '__main__':
    print("您正在把mymod.py 当成主模块执行")
else:
    print("mymod.py 不是主模块")
