# 练习:
#   写一个程序,打印一个高度为4行的矩形方框
#     要求输入一个整数,此整数代表矩形的宽度,输出矩形
#   如:
#     请输入矩形宽度: 10
#   打印:
#     ##########
#     #        #
#     #        #
#     ##########
#   如:
#     请输入矩形宽度: 5
#   打印:
#     #####
#     #   #
#     #   #
#     #####

w = int(input("请输入矩形宽度: "))
print('#' * w)
print('#', ' ' * (w - 2), '#', sep='')
print('#', ' ' * (w - 2), '#', sep='')
print('#' * w)



