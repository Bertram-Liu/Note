# text.py

import tkinter

root = tkinter.Tk()

text = tkinter.Text(root, width=50, height=3)
# 加入一行文字
text.insert(tkinter.END, '这是第一行')
text.pack()

root.mainloop()