# override.py


# 此示例示意覆盖的用法
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print("B.work被调用!!!!")
    pass

b = B()
b.work()  # 请问调用谁?  B.work被调用

a = A()
a.work()  # 请问调用谁?




