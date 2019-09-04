# property.py

# 实例属性不能直接对取值和赋值加以控制
class Student:
    def __init__(self, s=100):
        self.score = s
    
s1 = Student(59)

scr = s1.score  # 取值

print("成绩是:", scr)

s1.score = 9999999  # 赋值

print('成绩是:', s1.score)

