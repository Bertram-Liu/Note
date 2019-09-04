#   1. 输入一个整数,代表一棵圣诞树的树干高度
#     打印一棵圣诞树
#     如:
#       输入: 2
#     打印
#      *
#     ***
#      *
#      *
#     如:
#       输入: 3
#     打印:
#       *
#      ***
#     *****
#       *
#       *
#       *

n = int(input("请输入树干的高度: "))

# 方法1, 生成星号字符串,然后再次字符串居中显示实现
# max_width = n * 2 - 1  # 树冠最下一层的宽度
# for line in range(1, n + 1):  # line 代表行号
#     star = line * 2 - 1  # 计算每一行的星号个数
#     stars = '*' * star  # 形成字符串
#     print(stars.center(max_width))  # 居中显示字符串
# # 打印树干部分:
# for _ in range(n):  # 循环n次
#     stars = '*'.center(max_width)  # 将一个星号居中显录
#     print(stars)

# 方法2 用左侧添加空格的方式来实现的印树
for line in range(1, n + 1):  # line 代表树冠的行数
    stars = '*' * (line * 2 - 1)  # 计算星号字符串
    blank = ' ' * (n - line)    # 计算左侧空格的个数和字符串
    print(blank + stars)

for _ in range(n):
    blank = ' ' * (n - 1)  # 左侧空格个数和字符串
    print(blank + '*')












