# file : mypack/games/contra.py


def play():
    print("正在玩魂斗罗")

def game_over():
    print("魂斗罗游戏结束!")
    # 调用mypack.menu 里的show_menu
    # 1. 用绝对导入
    from mypack.menu import show_menu
    show_menu()
    # 2. 相对导入
    from ..menu import show_menu
    show_menu() 
    # 3. 如下相对导入会出错
    # 相对导入时不能超出包的外部
    # from ...mypack.menu import show_menu  # 出错



print("魂斗罗模块被加载!")
