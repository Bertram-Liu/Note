# super_init.py


class Human(object):
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print("Human.__init__被调用", n, a)

    def show_info(self):
        print("姓名:", self.name)
        print("年龄:", self.age)

class Student(Human):
    def __init__(self, n, a, s):
        super().__init__(n, a)
        print("Student.__init__(", n, a, s, ')')
        self.score = s

    def show_info(self):
        super().show_info()
        print("成绩:", self.score)

s1 = Student('李四', 25, 100)
s1.show_info()
# print(dir(s1))

# h1 = Human('小张', 20)  # 请问是否会调用__init__方法？
# h1.show_info()


