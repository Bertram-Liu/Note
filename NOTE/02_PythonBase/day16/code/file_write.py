# file_write.py

# 此示例示意文本文件的写操作

try:
    fw = open("mynote.txt", 'w')  # 'w' 只写模式

    fw.write("你好!\n")  # w写入字符串
    fw.write("ABC")

    fw.writelines(["这是第一行\n", '这是第二行\n'])

    fw.close()
except OSError:
    print("打开文件失败!")