#   3. 给出一个年份判断是否是闰年并打印结果
#      规则: 每四年一闰,每百年不闰,四百年又闰
#      如:
#         2016年闰年, 2100年非闰年, 2400年 闰年


y = int(input("请输入年:"))

if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print(y, '是闰年')
else:
    print(y, '不是闰年')