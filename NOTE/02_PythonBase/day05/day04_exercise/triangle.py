#   3. 用while语句实现打印三角形,输入一个整数,表求三角形的宽度和高度
#     打印出相应的直角三角形
#     如:
#       请输入三角形的宽度: 4
#       1) 打印如下:
#         *
#         **
#         ***
#         ****
#       2) 打印如下:
#            *
#           **
#          ***
#         ****
#       3) 打印如下三角形:
#         ****
#         ***
#         **
#         *
#       4) 打印如下三角形:
#         ****
#          ***
#           **
#            *


w = int(input("请输入三角形的宽度:"))

line = 1  # line 代表当前行数
while line <= w:
    # 打印一行
    star = line  # star 代表星号个数
    print('*' * star)
    line += 1

print('--------------------')
line = 1
while line <= w:
    star = line  # 星号个数
    blank = w - star  # 求空格的个数
    print(' ' * blank + '*' * star)
    line += 1

print('--------------------')
star = w  # star 代表当前行的星号个数
while star > 0:
    print('*' *  star)
    star -= 1

print('--------------------')
star = w
while star > 0:
    blank = w - star  # 计算空格个数
    print(' ' * blank + '*' * star)
    star -= 1

#   4) 打印如下三角形:
#     ****
#      ***
#       **
#        *

