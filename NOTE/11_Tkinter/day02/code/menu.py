# menu.py

import tkinter
root = tkinter.Tk()

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label='打开')
filemenu.add_command(label='保存')
filemenu.add_command(label='退出', command=root.destroy)
menubar.add_cascade(menu=filemenu, label='文件')

editmenu = tkinter.Menu(menubar)  # 创建别一个子菜单
editmenu.add_command(label='复制')
editmenu.add_command(label='剪切')
editmenu.add_command(label='粘帖')
menubar.add_cascade(menu=editmenu, label='编辑')

root.config(menu=menubar)  # 把menubar 添加到主窗口上

root.mainloop()

