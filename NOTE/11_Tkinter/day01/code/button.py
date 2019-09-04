# button.py


# 此示例示意Tkinter 中 Button 的用法

import tkinter
root = tkinter.Tk()

def onBtn():
    print("按钮被点击")

btn1 = tkinter.Button(root, text='点点我试试',
                      bg='yellow',
                      width=20,
                      command=onBtn
                      )
btn1.pack()

root.mainloop()