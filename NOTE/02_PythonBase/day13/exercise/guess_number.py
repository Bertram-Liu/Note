# 练习:
#   猜数字游戏
#     随机生成一个0~100之间的整数,用变量x绑定
#     让用户输入一个数用y绑定.输入猜数字的结果
#       如果y等于生成的数x,则提示: "恭喜您猜对了"
#       如果y 大于 x, 则提示: "您猜的数字大了"
#       如果y 小于 x, 则提示: "您猜的数字小了"
#     循环让用户输入.直到猜对为止,显示用户猜数字的次数后
#     退出程序
  
import random

x = random.randint(0, 100)
# print(x)
times = 0  # 用来记录猜的次数

while True:
    y = int(input('请输入整数(0~100): '))
    times += 1
    if y > x:
        print("您猜的数字大了")
    elif y < x:
        print("您猜的数字小了")
    else:
        print("恭喜您猜对了")
        break

print("您共猜了%d次" % times)



