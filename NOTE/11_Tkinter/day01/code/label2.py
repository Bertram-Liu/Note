# label1.py

# Label 示例

import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, text='标签1',
                             bg='#00FF00',
                             fg='blue',
                             width=10,
                             height=3
                             )
label1.pack()
label2 = tkinter.Label(root, text='标签2',
                      bg='orange', 
                      font=('宋体', 40, 'bold')
                      )
label2.pack()  # 放入主窗口
label3 = tkinter.Label(root, text='标签2',
                      bg='orange', 
                      font=('宋体', 40, 'normal')
                      )
label3.pack()  # 放入主窗口

# 创建一张图片
img = tkinter.PhotoImage(file='mybutton.gif')

label4 = tkinter.Label(root, text="图片",
                      image=img
                      )
label4.pack()  # 放入主窗口
root.mainloop()
