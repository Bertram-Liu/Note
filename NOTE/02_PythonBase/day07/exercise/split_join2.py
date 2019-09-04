# 练习:
#   有字符串"hello", 生成字符串"h e l l o" 和 "h-e-l-l-o"

s = 'hello'
# L = []
# for ch in s:
#     L.append(ch)
L = list(s)

print(L)
s2 = ' '.join(L)
print("s2=", s2)
s3 = '-'.join(L)
print('s3=', s3)

