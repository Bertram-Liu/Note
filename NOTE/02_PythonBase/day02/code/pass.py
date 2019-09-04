# pass.py

# 写程序输入一个学生的成绩:
# 如果成绩在0~100之间为正常值,否则报错

score = int(input("请输入学生成绩: "))

if 0 <= score <= 100:
    # print("正常值")
    pass
else:
    print("成绩不在合法的范围内!!!")

