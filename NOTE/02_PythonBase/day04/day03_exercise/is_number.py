#   3. 输入一段字符串,写程序判断您输入的文字是否全是数字.
#     如果是数字,将您输入的数字加1后打印出来!

s = input("请输入文字: ")

if s.isdigit():
    print("您输入的是数字")
    x = int(s)  # 不会报错
    print(s, '加1得', x + 1)
else:
    print("您输入的不是数字")