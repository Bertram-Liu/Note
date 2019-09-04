# mynumber.py

# 此示例示意自定义的类，添加相应方法，让此类的对象能够使用
# 运算符进行操作

class MyNumber:
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        return "MyNumber(%s)" % self.data

    def __add__(self, other):
        v = self.data + other.data
        return MyNumber(v)  # 创建新对象并返回

    def __sub__(self, rhs):
        return MyNumber(self.data - rhs.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)
n3 = n1 + n2  # 等同于 n3=n1.__add__(n2)
print(n1, "+", n2, '=', n3)
n4 = n1 - n2
print(n4)  # MyNumber(-100)




