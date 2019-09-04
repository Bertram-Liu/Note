# with3.py


class A:
    def __enter__(self):
        '''此方法必须返回由as绑定的对象'''
        print("已进入with语句")
        return self

    def __exit__(self, e_type, e_value, e_traceback):
        print("已离开with语句")
        if e_type is None:
            print("离开with时没有发生异常")
        else:
            print("离开with时有异常发生")
            print("e_type:", e_type)
            print("e_value:", e_value)
            print("e_traceback:", e_traceback)

# a = A()
with A() as a:
    x = int(input("请输入: "))




