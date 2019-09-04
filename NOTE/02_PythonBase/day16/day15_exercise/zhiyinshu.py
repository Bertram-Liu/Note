#   5. 分解质因数,输入一个正整数,分析质因数
#     如
#       输入: 90
#     打印:
#       90 = 2*3*3*5
#       (质因数是的指最小能被原数整除的系数(不包括1))

def get_zhiyinshu(x):
    '''如x=90
    返回: [2, 3, 3, 5]
    '''
    L = []
    while x > 1:  # 它一定至少有一个质因数
        for i in range(2, x + 1):
            if x % i == 0:  # i为x的质因数
                L.append(i)
                # 修改正x的下一次的值
                x = int(x / i)
                break  # 终止本次打开
    return L


n = int(input("请输入一个整数: "))
L = get_zhiyinshu(n)
L2 = [str(x) for x in L]
s = str(n) + '=' + '*'.join(L2)
print(s)

