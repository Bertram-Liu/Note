#   2. 输入一年中的月份(1~12) 输出这个月在哪儿个季度,如果输入
#     的是其它的数,则提示您输错了
  

m = int(input("请输入月份(1~12): "))

if 1 <= m <= 12:
    print("当前月份合法")
    if m <= 3:
        print("春季")
    elif m <= 6:
        print("夏季")
    elif m <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您输错了!")


# if 1 <= m <= 3:
#     print("春季")
# elif 4 <= m <= 6:
#     print("夏季")
# elif 7 <= m <= 9:
#     print("秋季")
# elif 10 <= m <= 12:
#     print("冬季")
# else:
#     print('您输错了!!')
