#   写一个程序,输入联系人的电话号码和姓名,
#     把这些姓名和电话号码记录在文件中存储,
#     如:
#       请输入姓名: 张三
#       请输入电话: 13888888888
#       请输入姓名: 李四
#       请输入电话: 13999999999
#       请输入姓名: <直接回车结束输入>
#     格式为:
#       张三 1388888888
#       李四 1399999999

try:
    fw = open("phone.txt", 'w')
    while True:
        name = input("请输入姓名: ")
        if not name:
            break
        number = input("请输入电话: ")
        fw.write(name)
        fw.write(' ')
        fw.write(number)
        fw.write('\n')
    fw.close()
except OSError:
    print("操作失败!")
