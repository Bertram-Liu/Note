# 练习:
#   写一个程序,输入你的出生年月日,
#     1) 算出你已经出生多少天?
#     2) 算出你出生那天是星期几?

import time

year = int(input("请输入生成的年:"))
month = int(input("请输入生成的月:"))
day = int(input("请输入生成的日:"))
birth_tuple = (year, month, day, 0, 0, 0, 0, 0, 0)
birth_time = time.mktime(birth_tuple)
life_time =time.time() - birth_time  # 代表出生到现在过了多少少
life_days = life_time / 3600 // 24 # 代表出生的天数
print('您已生出:', life_days, '天')

t = time.localtime(birth_time)  # 得到出生的时间元组
week = {
    0: '一',
    1: '二',
    2: '三',
    3: '四',
    4: '五',
    5: '六',
    6: '日'
}
print("您出生那天是星期", week[t[6]])
