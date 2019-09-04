# label1.py

# Label 示例

import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, text='标签1',
                             bg='red',
                             fg='blue',
                             width=10,
                             height=3
                             )
label1.pack()

root.mainloop()
