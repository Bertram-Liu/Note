# 看懂下列代码在做什么事?

def myinput(fn):
    L = [1, 5, 3, 9, 7]
    r = fn(L)
    return r

print(myinput(max))  # 9
print(myinput(min))  # 1
print(myinput(sum))  # 25
