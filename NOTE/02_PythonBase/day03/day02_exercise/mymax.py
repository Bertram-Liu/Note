#   2. 写一个程序,输入三个数,打印出三个数中的最大数
#      (思考:如果是四个数,五个数打印出最大数该如何做?)


a = int(input("请输入第一个数: "))
b = int(input("请输入第二个数: "))
c = int(input("请输入第三个数: "))

if a > b:
    # a大
    if a > c:
        print(a)
    else:
        print(c)
else:
    # b大
    if b > c:
        print(b)
    else:
        print(c)