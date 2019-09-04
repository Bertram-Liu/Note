# def2.py

# 此示例示意自定义带有两个参数的函数,
# 此函数用来打印用户调用的两个实参数字的最大值

def mymax(a, b):
    print('a=', a)
    print('b=', b)
    if a > b:
        print(a, "大于", b)
    else:
        print(a, "小于等于", b)

mymax(5, 10)
mymax(200, 100)
mymax("ABC", "abc")



