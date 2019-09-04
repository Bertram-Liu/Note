#   2. 写一个程序,输入一段字符串,判断这个字符串中有几个英文字母
#     (英文字母是指a-z A-Z的英文)


s = input("请输入一段字符串: ")
i = 0
english_count = 0  # 用来记录英文字母的个数
while i < len(s):
    ch = s[i]
    # 在此外统计英文字符的个数
    # if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
    if 65 <= ord(ch) < 65+26 \
        or ord('a') <= ord(ch) <= ord('z'):
        english_count += 1
    i += 1  # 移向下一个索引


print("英文字母的个数是:", english_count)