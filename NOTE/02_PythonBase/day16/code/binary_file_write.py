# binary_file_write.py

# 此示例示意二进制文件的写操作

try:
    fw = open("mybin.txt", 'wb')  # w写,b二进制

    b = bytes(range(256))
    count = fw.write(b)
    print("成功写入了", count, '个字节!')  # 256

    fw.close()
except OSError:
    print("打开mybin.txt出错")

