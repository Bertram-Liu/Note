# 练习:
#     names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#     排序的依据是最后一个字符的编码值大小,如果最后一个,依次
#     向前对比,即依据为:
#             'moT'   'yrreJ'   'ekipS'  'ekyT'
#     排序后结果为:
#         ['Spike', 'Tyke', 'Tom', 'Jerry']


names = ['Tom', 'Jerry', 'Spike', 'Tyke']

def getkey(x):
    r = x[::-1]  # 根据给定的x,返回x的依据
    print(x, '的依据是:', r)
    return r  

result = sorted(names, key=getkey)
print(result)  # 结果 ['Spike', 'Tyke', 'Tom', 'Jerry']


