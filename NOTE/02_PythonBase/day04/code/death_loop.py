# death_loop.py

# 写一个机器人程序,
#     问           答
#    你好        有什么能帮助您
#    你叫什么名字  机器人
#    再见        欢迎再来(退出程序)

while True:
    s = input("请问:")
    if s == '你好':
        print("有什么能帮助您")
    elif s == '你叫什么名字':
        print("机器人")
    elif s == '再见':
        print("欢迎再来")
        break



