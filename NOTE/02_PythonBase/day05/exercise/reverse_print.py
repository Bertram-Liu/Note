# 练习:
#   输入一个字符串,从尾向头输出这个字符串的字符
#   如:
#     请输入: ABC中文
#   打印:
#     文
#     中
#     C
#     B
#     A

s = input("请输入: ")
# 方法1 用for语句实现
# for ch in s[::-1]:
#     print(ch)

# 方法2 用while语句实现
i = len(s) -1   # i代表索引, i绑定最后一个元素的索引
while i >= 0:
    print(s[i])
    i -= 1

