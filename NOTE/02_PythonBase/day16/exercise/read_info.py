# 练习:
#   自己写一个文件'info.txt' 内部存一些文字信息
#     张三,20,100
#     李四,21,96
#     小王,19,98
#   写程序将这些数据读取出来,并以如下格式打印在屏幕终端上:
#     张三 今年 20 岁,成绩是: 100
#     李四 今年 21 岁,成绩是: 96
#     小王 今年 19 岁,成绩是: 98

try:
    # 打开文件
    fr = open("info.txt")
    # 读取文件并处理
    while True:
        line = fr.readline()
        if not line:
            break  # 已读取到行尾
        s = line.strip()  # line='小张,20,100\n'
        L = s.split(',')  # L =['小张', '20', '100']
        name, age, score = L
        age = int(age)
        score = int(score)
        print(name, '今年', age, '岁,成绩:', score)

    # 关闭文件
    fr.close()
except OSError:
    print("打开info.txt失败")
