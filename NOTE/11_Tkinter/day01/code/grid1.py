# 此示例示意网络布局


import tkinter
root = tkinter.Tk()

btn1 = tkinter.Button(root, text='按钮1')
btn1.grid(row=0, column=0, stick=tkinter.NW)

btn2 = tkinter.Button(root, text='按钮2')
btn2.grid(row=1, column=1)

btn3 = tkinter.Button(root, text='按钮3')
btn3.grid(row=2, column=2)

label1 = tkinter.Label(root, text="Label1111111111",
           bg='red')
label1.grid(row=1, column=0, rowspan=2, columnspan=1)

label2=tkinter.Label(root, text="Label2",bg='blue',
                     height=3)
label2.grid(row=0, column=1, rowspan=1, columnspan=2)


root.mainloop()



