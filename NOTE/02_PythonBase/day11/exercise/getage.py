# 练习:
#   已知有五位朋友在一起
#   　第五位朋友比第四位大2岁
#   　第四位朋友比第三位大2岁
#   　第三位朋友比第二位大2岁
#   　第二位朋友比第一位大2岁
#   　第一位朋友说他10岁
#   编写函数，算出第五位朋友几岁，第三位朋友几岁?

def get_age(n):
    if n == 1:
        return 10
    return get_age(n-1) + 2

print("第五位朋友：", get_age(5), '岁')
print("第三位朋友：", get_age(3), '岁')
