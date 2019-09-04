# static_method.py

# 此示例示意静态方法的定义和调用

class A:
    @staticmethod
    def myadd(x, y):
        return x + y
    
print(A.myadd(100, 200))  # 300
a = A()
print(a.myadd(3, 4))  # 7



