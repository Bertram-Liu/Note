#   2. 写程序生成如下字符串:
#     1)  'ABCDE........XYZ'

#     2)  'AaBbCcDdEe.....XxYyZz'
#       (提示: 可以使用 ord 和 chr 函数实现)


# 1)  'ABCDE........XYZ'
s = ''  # 此变量用来绑定生成的结果 
for code in range(65, 65 + 26):
    ch = chr(code)
    # print(ch)
    s = s + ch  # s += ch

print("s=", s)

# 2)  'AaBbCcDdEe.....XxYyZz'
s = ''
for code in range(65, 65 + 26):
    s += chr(code)  # 追加大写字母
    s += chr(code + 32)  # 追加小写字母

print("s=", s)
