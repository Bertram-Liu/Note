# spinbox.py


import tkinter
root = tkinter.Tk()

spin1 = tkinter.Spinbox(root, from_=0,
                        to=100, increment=5)
spin1.pack()

root.mainloop()
