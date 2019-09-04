# entry.py

# 此示例示意用entry来输入数据,用button来读取entry里的内容

import tkinter
root = tkinter.Tk()

entry1 = tkinter.Entry(root)
entry1.pack()

def onBtn():
    s = entry1.get()  # 读取Entry中的数据
    print(s)
    label1.config(text='====' + s + '====')

btn1 = tkinter.Button(root, text='点我读数据...',
                      command=onBtn)
btn1.pack()

label1 = tkinter.Label(root, text='xxxxxx')
label1.pack()

root.mainloop()