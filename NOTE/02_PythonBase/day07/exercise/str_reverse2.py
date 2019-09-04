# 练习:
#   任意输入一个字符串,将此字符串中的空格全部去掉,生成反转
#   后的字符串
#   如:
#     请输入: abc  def   g
#   生成如下字符串:
#     s2 = 'gfedcba'
#     print(s2)  # gfedcba
#     提示: 可以用reversed进行反转

s = input("请输入: ")
# s2 = s.replace(' ', '')  # 去掉空格
# s2 = s2[::-1]
s2 = ''
for ch in reversed(s):  # 反向遍历字符串中的元素
    if ch != ' ':
        s2 += ch

print(s2)