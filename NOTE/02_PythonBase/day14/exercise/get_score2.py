# 练习:
#   写一个函数 get_score() 来获取学生输入的成绩 (0~100)的整数
#   如果输入的不是0~100的整数,则此函数返回0,
#   如:
#     def get_score():
#         s = input("请输入成绩: ")
#         ...  # 此处自己实现
#     score = get_score()
#     print("学生的成绩是:", score)

def get_score():
    s = input("请输入成绩: ")
    try:
        scr = int(s)
        if 0 <= scr <= 100:
            return scr
        return 0

    except ValueError:
        return 0

score = get_score()
print("学生的成绩是:", score)
