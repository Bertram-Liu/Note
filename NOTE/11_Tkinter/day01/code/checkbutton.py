#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter
root = tkinter.Tk()

def kanshu():
    print("看书按钮被按下")
    # check_btn.get()

check_btn = tkinter.Checkbutton(root, text='看书',
                               command=kanshu)
check_btn.pack()

check_btn2 = tkinter.Checkbutton(root, text='看电影')
check_btn2.pack()

btn1 = tkinter.Button(root, text='禁止看书',
            command=lambda: check_btn.deselect())
btn1.pack()
btn2 = tkinter.Button(root, text='必须看书',
            command=lambda: check_btn.select())
btn2.pack()
root.mainloop()