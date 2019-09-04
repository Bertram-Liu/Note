# property.py

# 实例属性不能直接对取值和赋值加以控制
class Student:
    def __init__(self, s):
        self.__score = s

    def get_score(self):
        print('get_score被调用!')
        return self.__score

    def set_score(self, s):
        assert 0 <= s <= 100, '成绩不在合法范围内!!!'
        self.__score = s
    
    score = property(get_score)
    score = score.setter(set_score)

s1 = Student(59)
scr = s1.score  # 代替 scr = s1.get_score()
print("成绩是:", scr)
s1.score = 88
# s1.score = 99999999  # s1.set_score(9999999)
print('成绩是:', s1.score)

