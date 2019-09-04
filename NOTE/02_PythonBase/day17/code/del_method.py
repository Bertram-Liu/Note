# del_method.py

# 此示例示意__del__方法的用法

class Car:
    def __init__(self, info):
        self.info = info
        print("汽车", info, '被创建!')
        # self.file = open('xxx.txt')  # 打开

    def __del__(self):
        '''析构方法不能有其它形参'''
        print('汽车', self.info, '对象被销毁')
        # self.file.close()  # 关闭文件
        

c1 = Car('BYD F3')
L = [1, 2, 3]
L.append(c1)
del c1

s = input("程序暂停.请输入回车键继续... ")
# while True:
#     pass

print("程序结束!!!")
