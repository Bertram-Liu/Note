# 练习:
#   1. 任意输入一段字符串
#     1) 计算出这段字符串中空格的个数,并打印这个数
#     2) 计算出字符串的全部ascii字符的个数并打印
#         注:  ascii 字符的编码在0~127范围内
#     思考:
#       用while语句能实现上述功能?

s = input("请输入一段文字: ")

blanks_count = 0  # 用来记录空格的个数

# for c in s:
#     if c == ' ':  # if ord(c) == 32:
#         blanks_count += 1

i = 0  # i 代表索引值
while i < len(s):
    c = s[i]
    if c == ' ':
        blanks_count += 1
    i += 1

print("空格的个数是:", blanks_count)

ascii_count = 0
for c in s:
    if ord(c) <= 127:
        ascii_count += 1
print("ascii字符的个数是:", ascii_count)



