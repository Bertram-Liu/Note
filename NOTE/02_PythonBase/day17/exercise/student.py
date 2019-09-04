# 练习:
#   写一个学生类 Student 类,此类用于描述学生信息,学生信息有:
#     姓名,年龄,成绩(默认为0)
#     1) 为该类添加初始化方法,实现在创建对象时自动创建'姓名',
#        '年龄', '成绩' 属性
#     2) 添加 set_score 方法能为对象修改成绩信息
#     3) 添加show_info方法打印学生对象的信息
#   如:
#     class Student:
#         def __init__(...):
#             ...
#         def set_score(self, score):
#             ...
#         def show_info(self):
#             ...
#     L = []
#     L.append(Student('小张', 20, 100))
#     L.append(Student('小李', 18, 95))
#     L.append(Student('小赵', 19))
#     L[-1].set_score(70)  # 为小赵修改成绩
#     for s in L:
#         s.show_info()  # 显示所有学生信息



class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    def set_score(self, score):
        self.score = score

    def show_info(self):
        print(self.name, self.age, '岁, 成绩:', self.score)
L = []
L.append(Student('小张', 20, 100))
L.append(Student('小李', 18, 95))
L.append(Student('小赵', 19))
# print(L)
for s in L:
    s.show_info()  # 显示所有学生信息
print("-----------修改成绩后-------")
L[-1].set_score(70)  # 为小赵修改成绩
for s in L:
    s.show_info()  # 显示所有学生信息
