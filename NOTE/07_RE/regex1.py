import re 

s = "2019年4月28日"
pattern = r'\d+'

it = re.finditer(pattern,s)

# print(dir(next(it)))

for i in it:
    print(i.group()) # 获取match对象匹配到的内容

#　完全匹配
obj = re.fullmatch(r'\w+','hello_1949')
print(obj.group())

#　匹配开头
obj = re.match(r'[A-Z]\w+',"Hello,Jame")
print(obj.group())

#　匹配第一处
obj = re.search(r'\d+',"今天2018-1-19")
print(obj.group())