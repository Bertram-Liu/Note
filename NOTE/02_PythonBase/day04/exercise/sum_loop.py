# 练习:
#   任意输入一些整数,当输入负数时结束输入
#   当入完毕后,打印出您输入的全部正整数的和
#   如:
#     请输入: 1
#     请输入: 2
#     请输入: 3
#     请输入: 4
#     请输入: -1
#   打印:
#     您刚才输入的这些数的和是: 10

s = 0  # 此变量用来累加所有正整数
while True:
    x = int(input("请输入: "))
    if x >= 0:
        s += x
    else:
        break

print("您刚才输入的这些数的和是:", s)

