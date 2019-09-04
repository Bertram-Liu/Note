# listbox.py

import tkinter

root = tkinter.Tk()

listbox = tkinter.Listbox(root)
listbox.insert(tkinter.END, '体育')
listbox.insert(tkinter.END, '音乐')
listbox.insert(tkinter.END, '美术')

listbox.pack()

root.mainloop()