# named_keyword_args.py

# 此示例示意命名关键字形参的定义方式和调用方法
def func(a, b, *args, c, d):
    print(a, b, args, c, d)


# func(1, 2, 3, 4, 5, 6, 7, 8)  # 出错
func(1, 2, 3, 4, c=30, d=40)


