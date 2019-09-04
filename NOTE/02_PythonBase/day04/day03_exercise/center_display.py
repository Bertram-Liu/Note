#   2. 输入三行文字,让这三行文字在一个方框居中显示
#     (注:不要输入中文)
#     如:
#       请输入: hello!
#       请输入: I'm studing python!
#       请输入: I like python!
#     显示如下:
#       +---------------------+
#       |        hello!       |
#       | I'm studing python! |
#       |   I like python!    |
#       +---------------------+

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

max_len = max(len(a), len(b), len(c))

line1 = '+-' + '-' * max_len + '-+'
print(line1)
print('| ' + a.center(max_len) + ' |')
print('| ' + b.center(max_len) + ' |')
print('| ' + c.center(max_len) + ' |')
print(line1)