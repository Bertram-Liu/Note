# star_tuple_args.py

# 此示例示意星号元组形参的定义方式和用法
def func(*args):
    print("实参的个数是:", len(args))
    print("args=", args)

func()  # 无参
func(1, 2, 3, 4)
func(100, 200, 300, 400, 500, 600)

