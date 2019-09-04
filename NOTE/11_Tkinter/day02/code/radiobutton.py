# radiobutton.py

import tkinter
root = tkinter.Tk()

def radiobtn_clicked():
    if sex_value.get() == 1:
        print("您选中的是男")
    elif sex_value.get() == 0:
        print("您选中的是女")
# 定义一个整数关联变量来关联这两个radiobutton
sex_value = tkinter.IntVar()

nan = tkinter.Radiobutton(root, text='男', value=1,
                         variable=sex_value,
                         command=radiobtn_clicked)

nv = tkinter.Radiobutton(root, text='女', value=0,
                        variable=sex_value,
                        command=radiobtn_clicked)

sex_value.set(1)

nan.pack()
nv.pack()


root.mainloop()