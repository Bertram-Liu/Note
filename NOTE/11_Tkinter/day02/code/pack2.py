# pack1.py

import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, bg='red', text='顶')
label2 = tkinter.Label(root, bg='blue', text='左下')
label3 = tkinter.Label(root, bg='green', text='右下')

label1.pack()
label2.pack(side=tkinter.LEFT)
label3.pack(side=tkinter.RIGHT)

root.mainloop()
