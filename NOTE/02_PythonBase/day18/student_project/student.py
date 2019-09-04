# student.py


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def get_infos(self):
        return (self.name, self.age, self.score)

    def get_name(self):
        return self.name
    
    def set_score(self, s):
        assert 0 <= s <= 100, '成绩超出范围！'
        self.score = s

    def get_score(self):
        return self.score
    
    def get_age(self):
        return self.age

        