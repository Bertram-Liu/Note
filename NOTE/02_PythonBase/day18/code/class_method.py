# class_method.py

# 此示例示意类方法的定义规则和调用
class A:
    v = 0  # 类属性

    @classmethod
    def get_v(cls):  # cls为class简写
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value

print(A.get_v())  # ???
a = A()
print(a.get_v())
A.set_v(100)
print(A.get_v()) # 100
a.set_v(200)
print(A.get_v())  # 200


