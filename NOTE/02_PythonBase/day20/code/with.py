# with.py

# 此示例示意with语句的语法和用法
# 打开../day20.txt 读出文件的第一行

try:
    fr = open('../day20.txt')
    try:
        s = fr.readline()
        print("第一行是:", s)
        int(input("请制造错误："))
    finally:
        fr.close()
        print("操作成功")
except OSError:
    print("打开文件失败")





