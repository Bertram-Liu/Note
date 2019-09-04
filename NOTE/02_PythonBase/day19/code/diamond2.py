# diamond.py


# 此示例示意钻石继承(棱形继承)的问题
class A:
    def go(self):
        print("A")

class B(A):
    def go(self):
        print("B")
        super().go()  # C

class C(A):
    def go(self):
        print("C")
        super().go()   # A

class D(B, C):
    def go(self):
        print('D')
        super().go()  # super(D, self).go()  B

d = D()
d.go()  # ???




