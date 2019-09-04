# try_finally.py


def fry_egg():
    print("打开天燃气...")
    try:
        count = int(input("请输入鸡蛋个数: "))
        print("完成煎鸡蛋,共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天燃气")  # 必须要做的事儿


fry_egg()

