# mystudent.py


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s
    
    def __repr__(self):
        s = 'Student(%r, %d, %d)' % (self.name,
                                     self.age,
                                     self.score)
        return s
    
a = Student("小张", 20, 100)
b = Student('小李', 18, 98)
L = []
L.append(a)
L.append(b)
print(L)  # sys.stdout.write(字符串)

# def myprint(L):
#     s = str(L)
#     sys.stdout.write(s)