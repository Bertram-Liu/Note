# seek.py

fr = open('20bytes.txt', 'rb')

print("当前读写位置是:", fr.tell())  # 0
b = fr.read(2)
print(b)  # b'AB'
print("当前读写位置是:", fr.tell())  # 2

# 读写abcde这五个字节
# 1. fr.seek(5, 0)  # 从文件头向后移动5个字节
# 2. fr.seek(3, 1)  # 从前向位置向后移动3个
fr.seek(-15, 2)  # 从文件尾向前移动15个字节


b = fr.read(5)  # b=b'abcde'
print(b)

