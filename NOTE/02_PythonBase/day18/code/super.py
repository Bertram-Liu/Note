# 此示例示意super函数的用法
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print("B.work被调用!!!!")
    
    def mywork(self):
        '''此方法内能否即调用自己的work方法，同时又调用
        父类的work方法?'''
        self.work()  # B.work被调用
        # A.work被调用
        super(B, self).work()
        super().work()  # A.work被调用

b = B()
b.work()  # B.work被调用
# A.work(b)  # A.work被调用
super(B, b).work()  # A.work被调用
print("----------------------------")
b.mywork()










