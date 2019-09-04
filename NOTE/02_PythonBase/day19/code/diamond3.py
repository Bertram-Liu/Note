# diamond.py


# 此示例示意钻石继承(棱形继承)的问题
class A:
    def go(self):
        print("A")

class B(A):
    def go(self):
        print("B")

class C(A):
    def go(self):
        print("C")

class D(B, C):
    def go(self):
        print('D')
        super(B, self).go()

d = D()
d.go()  # ???




