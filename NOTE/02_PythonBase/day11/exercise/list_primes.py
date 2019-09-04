#   2. 用filter函数将1~100之间所有的素数放到L列表中,再印出
#     这个列表.


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    
L = list(filter(is_prime, range(100)))
print(L)

