# mycal.py

import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root)
entry1.pack()  # 加入到主窗口
label_add = tkinter.Label(root, text='+',
                          font=('黑体', 20))
label_add.pack()

# 第二个数的输入框
entry2 = tkinter.Entry(root)
entry2.pack()
label_equal = tkinter.Label(root, text='=',
                            font=('黑体', 20))
label_equal.pack()

# 结果 
label_result = tkinter.Label(root)
label_result.pack()

# 开始计算按钮
def onCal():
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        s = str(n1 + n2)  # 转为字符串
        label_result.config(text=s)
    except:
        label_result.config(text='输入有误')

btn_cal = tkinter.Button(root, text='开始计算',
                        command=onCal)
btn_cal.pack()


root.mainloop()







