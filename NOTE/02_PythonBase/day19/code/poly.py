# poly.py

class A:
    def run(self):
        print("A")

class B(A):
    def run(self):
        print('B')

class C(B):
    def run(self):
        print("C")

def test(obj):
    obj.run()  # 请问调用谁?  # 此处体现出动态

a = A()
b = B()
c = C()

test(b)
test(c)