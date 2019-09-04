# double_star_dict_args.py

def func(**kwargs):
    print("实参个数是:", len(kwargs))
    print("关键字参数是:", kwargs)

func(a=1, b=2, c=3)  # kwargs={'a':1, 'b':2,'c':3}
func(x=100, name='tarena', age=17, z=999)

# func(1, 2, c=3, d=4)  # 出错