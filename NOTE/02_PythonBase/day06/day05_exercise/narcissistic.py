# 3. 算出 100 ~ 999以内的水仙花数(Narcissistic number)
#   水仙花数是指百位数的3次方 加上 十位数的3次方 加 个位数的
#   3次方等于原数的整数
#     如:  153 等于 1**3 + 5**3 + 3**3 ,则153是水仙花数

# 方法1:
for x in range(100, 1000):
    bai = x // 100  # 提取百位数字
    shi = x % 100 // 10  # 十位
    ge = x % 10  # 个位
    if x == bai ** 3 + shi ** 3 + ge ** 3:
        print(x)

print("-----方法2-------")
for x in range(100, 1000):
    s = str(x)  # 将x转为字符串用s绑定
    bai = int(s[0])  # 用切片提取一个字符
    shi = int(s[1])
    ge = int(s[2])
    if x == bai ** 3 + shi ** 3 + ge ** 3:
        print(x)

print("-----方法3-------")
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            # print(bai, shi, ge)
            x = bai * 100 + shi * 10 + ge
            if x == bai ** 3 + shi ** 3 + ge ** 3:
                print(x)













