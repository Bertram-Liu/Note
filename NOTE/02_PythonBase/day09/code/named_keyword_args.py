# named_keyword_args.py

# 此示例示意命名关键字形参的定义方式和调用方法
def func(a, b, *, c, d):
    print(a, b, c, d)


# func(1, 2, 3, 4)  # c和d必须以关键字方式传参
func(1, 2, c=30, d=40)
func(a=10, b=20, c=30, d=40)
d= {'c':300, 'd': 400}
func(1, 2, **d)  # 正确,等同于func(1, 2, c=300, d=400)
