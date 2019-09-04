import re 

pattern = r"(ab)cd(?P<pig>ef)"
s = 'abcdefghi'

#　获取ｍａｔｃｈ对象
obj = re.search(pattern,s)

# 属性变量
print(obj.pos)     #　目标字符串开始位置
print(obj.endpos) #  目标字符串结束位置
print(obj.re)     #　正则表达式
print(obj.string) # 目标字符串
print(obj.lastgroup) # 最后一组组名
print(obj.lastindex) # 最后一组序号

print("==================================")
#　属性函数
print(obj.span())
print(obj.start())
print(obj.end())
print(obj.groups())
print(obj.groupdict())

print(obj.group()) #０即默认值，获取整体匹配内容
print(obj.group(1)) #第一组对应内容
print(obj.group('pig')) # pig组对应内容
