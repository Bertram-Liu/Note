# test_mypack.py

import mypack.menu  # 导入mypack包里的menu模块

mypack.menu.show_menu()  # 调用mypack里的menu模
                         # 块里的show_menu函数

import mypack.menu as m
m.show_menu() 

from mypack.menu import show_menu
show_menu()

from mypack.menu import *
show_menu()

import mypack.games.contra  # 导入

mypack.games.contra.play()  # 调用 





