#   1. 输入一些单词和解释,将单词作为键,将解释作为值,将这些数据存
#      入到字典中,打印这个字典
#      然后, 循环 输入要查询的单词,给出单调相关的解释.如果字典中
#      不存在这些词则显示查无此词

# 录入字典信息
mydict = {}
while True:
    word = input("请输入单词: ")
    if word == '':
        break  # 结束输入
    trans = input("请输入解释: ")
    if not trans:  # 当trans为''时,它的布尔值为False
        break
    # 走到此处,单词和解释都成功录入,放到字典中
    mydict[word] = trans

print("词库是:", mydict)

# 提供查询单词的功能
while True:
    word = input("请输入您要查询的单词: ")
    if word in mydict:
        print("解释:", mydict[word])
    else:
        print("查无此词!!!")














