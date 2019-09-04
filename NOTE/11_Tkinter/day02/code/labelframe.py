# labelframe.py

import tkinter
root = tkinter.Tk()

mylabelframe = tkinter.LabelFrame(root, text='性别')
mylabelframe.pack()

nan = tkinter.Radiobutton(mylabelframe, text='男')
nv = tkinter.Radiobutton(mylabelframe, text='女')
nan.pack()
nv.pack()

mylabelframe2 = tkinter.LabelFrame(root, text='爱好')
mylabelframe2.pack()

checkbtn1 = tkinter.Checkbutton(mylabelframe2,
                 text='看电影')
checkbtn1.pack()

tkinter.Checkbutton(mylabelframe2, text='踢球').pack()

root.mainloop()





