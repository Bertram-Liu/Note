# binary_file_read.py

# 此示例示意用二进制方式读取文件

fr = open("myfile.txt", 'rb')  # 二进制方式读取文件

b = fr.read()  # b 绑定字节串

fr.close()

print("读取的内容是:", b)
print("字节串的长度是:", len(b))
s = b.decode()  # 将字节串手动转为字符串
print("字符串的长度是:", len(s))
print("字符串的内容是:", s)


