import re 

s = "zhang:1994  li:1995"
pattern = r'(\w+):(\d+)'

# l = re.findall(pattern,s)
# print(l)

regex = re.compile(pattern)
l = regex.findall(s,0,10)
print(l)

l = re.split(r'\s+','Hello      world')
print(l)

s = re.subn(r'垃圾','**','张三，垃圾,垃圾，垃圾',2)
print(s)