#   2. 求100以内有哪儿些整数 与 自身+1的乘积再对11求余等的结果
#      等于8
#         x * (x + 1) % 11 == 8


for x in range(100):
    if x * (x + 1) % 11 == 8:
        print(x)