# combobox.py

import tkinter
import tkinter.ttk  # ComboBox 类在ttk子包中

root = tkinter.Tk()

def onBomboSelect(event):
    '''此函数为combo 的事件处理函数'''
    print(event, "--->", combo.get())

combo = tkinter.ttk.Combobox(root, values=[
                 '白菜', '西红柿', '土豆'
                ], state='readonly')
combo.current(1)
combo.bind('<<ComboboxSelected>>', onBomboSelect)
combo.pack()

root.mainloop()