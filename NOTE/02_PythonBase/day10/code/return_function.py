# return_function.py

def get_function():
    s = input("请输入您要做的操作: ")
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 4, 8, 6, 10]
f = get_function()
r = f(L)
print(r)


