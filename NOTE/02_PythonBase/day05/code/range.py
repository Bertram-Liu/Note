# range.py

for x in range(4):
    print(x)  # 0 1 2 3

print("--------------")

for x in range(3, 6):
    print(x)

print("==============")
for x in range(1, 10, 2):
    print(x)  # 1 3 5 7 9

print("+++++++++++++++")
for x in range(5, 0, -2):
    print(x)
print("***************")
for x in range(4, 0):
    print(x)  # 此print函数不会被调用