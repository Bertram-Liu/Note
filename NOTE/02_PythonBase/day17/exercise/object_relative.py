# 练习:
#   有两个人:
#     1) 姓名: 张三, 年龄: 35
#     2) 姓名: 李四, 年龄: 15
#   行为:
#     1) 教别人学东西 teach
#     2) 赚钱 work
#     3) 借钱 borrow
#     4) 显示自己的信息 show_info
#   事情描述:
#     张三 教 李四 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚了 1000 元钱
#     李四 向 张三 借了 200 元钱
#     35 岁的 张三 有钱 800 元,它学会的技能: 王者荣耀
#     15 岁的 李四 有钱 200 元,它学会的技能: python
#   如:
#     class Human:
#         ...


class Human:
    def __init__(self, n, a):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 钱
        self.skill = []  # 技能
    # 1) 教别人学东西 teach
    def teach(self, other, skill):
        print(self.name, '教', other.name,
              '学', skill)
        other.skill.append(skill)  # other获得技能

    # 2) 赚钱 work
    def work(self, money):
        print(self.name, '上班赚了', money, '元钱')
        self.money += money
    # 3) 借钱 borrow
    def borrow(self, other, m):
        print(self.name, '向', other.name, '借了',
             m, '元钱')
        other.money -= m
        self.money += m
    # 4) 显示自己的信息 show_info
    def show_info(self):
        # print(self.age, '岁的', self.name, '有钱',
        #       self.money, '元,它学会的技能:',
        #       self.skill)
        print(self.age, '岁的', self.name, '有钱',
              self.money, '元,它学会的技能:',
              ','.join(self.skill) )

zhang3 = Human('张三', 35)
li4 = Human('李四', 15)

#     张三 教 李四 学 python
zhang3.teach(li4, 'Python')
#     李四 教 张三 学 王者荣耀
li4.teach(zhang3, '王者荣耀')
#     张三 上班赚了 1000 元钱
zhang3.work(1000)
#     李四 向 张三 借了 200 元钱
li4.borrow(zhang3, 200)
# 35 岁的 张三 有钱 800 元,它学会的技能: 王者荣耀
zhang3.show_info()
# 15 岁的 李四 有钱 200 元,它学会的技能: python
li4.show_info()

        

