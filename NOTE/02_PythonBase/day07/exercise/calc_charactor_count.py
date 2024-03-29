# 练习:
#   输入一段字符串,打印出这个字符串中出现过的字符及出现过的次数
#     如:
#       请输入: ABCDABCABA
#     打印:
#       A: 4次
#       B: 3次
#       D: 1次
#       C: 2次
#       注: 不要求打印的顺序
    
s = input("请输入: ")
d = {}   # 先创建一个空字典,准备保存字符及字符对应的个数
         # 键为字符,值为个数

for ch in s:  # 遍历取出每个字符
    # 如果ch 已经在字典中,说明之前出现过这个字符,将个数加1
    if ch in d:
        d[ch] += 1
    # 否则,这是第一次出现,用ch创建一个键,将个数设置为1
    else:
        d[ch] = 1

# print(d)
for k, v in d.items():
    print(k, ":", v, '次')
