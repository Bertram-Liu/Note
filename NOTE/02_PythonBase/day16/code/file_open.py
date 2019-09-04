# file_open.py

# 此示例示意文件的打开和关闭过程
# 1. 打开文件
# myf = open('myfile.txt')
try:
    # myf = open('/home/tarena/aid1901/pbase/day16/code/myfile.txt')
    myf = open("abcd.txt")  # 触发异常通知
    print("打开文件成功")

    # 2. 读/写文件

    # 3. 关闭文件
    myf.close()
    print("关闭文件成功")
except OSError:
    print("打开文件失败!!!")

