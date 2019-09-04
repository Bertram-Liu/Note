# scale.py

import tkinter
root = tkinter.Tk()

def onScale1Move(value):
    print("Scale1的值是:", value)

scale = tkinter.Scale(root)
scale.config(from_=20, to=150)  # 设置范围
scale['bg'] = 'red'  # 等同于scale.config(bg='red')
scale.set(100)  # 设置当前值
scale.config(command=onScale1Move)  # 绑定回调函数

scale.pack()

scale2 = tkinter.Scale(root,
                       orient=tkinter.HORIZONTAL)
scale2.pack()

root.mainloop()