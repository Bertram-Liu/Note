#   2. 计算出100以内的全部素数,将这些素数存于列表L中,最后打印出
#     这些素数

L = []  # 先创建一个容器,准备存入素数

for x in range(100):
    if x < 2:
        continue  # 开始下一次
    else:  # x >= 2
        for i in range(2, x):
            if x % i == 0:  # x不是素数
                break
        else:  # 走到此处,x一定是素数
            L.append(x)

print("全部的素数是:", L)

