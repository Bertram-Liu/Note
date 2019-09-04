#   2. 写一个程序,任意输入一个整数,判断是否是素数(prime)
#     素数(也叫质数),是只能被1和自身整除的正整数
#       如:  2   3   5    7    11   13   17   19 ...
#     提示:
#       可以用排除法: 当判断x是否为素数时,只要让x分别除以 
#         2,3,4,5,6,...,x-1, 只要有一次整除了,则x不是素数
#       否则x是素数

x = int(input("请输入一个正整数: "))
if x < 2:
    print(x, '不是素数')
else:  # x一定大于等于2
    flag = True  # flag 标识,先假设x是素数,
    for i in range(2, x):
        # 让x除以i,只要被整数，则x不是素数
        if x % i == 0:
            print(x, '不是素数')
            flag = False  # 当不是素数时放倒旗子
            break
    # 走到此外，如果if 条件没有成立过，则x一定是素数
    if flag:
        print(x, '是素数')
