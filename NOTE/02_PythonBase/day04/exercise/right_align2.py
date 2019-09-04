# 练习:
#   输入三行文字,让这三行文字依次以20个字符的宽度右对齐
#   打印在终端上
#   如:
#     请输入第1行: hello china
#     请输入第2行: abcd
#     请输入第3行: a
#   输出结果为:
#         hello china
#                abcd
#                   a
#   做完上题后再思考:
#     能否以最长字符串的长度进行右对齐显示(左侧填充空格)

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

max_len = len(a)
if len(b) > max_len:
    max_len = len(b)
if len(c) > max_len:
    max_len = len(c)
print("最大长度是:", max_len)

print(' ' * (max_len-len(a)) + a)
print(' ' * (max_len-len(b)) + b)
print(' ' * (max_len-len(c)) + c)