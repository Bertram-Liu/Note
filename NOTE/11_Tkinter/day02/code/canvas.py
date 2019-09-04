# canvas.py


import tkinter
root = tkinter.Tk()

cvs = tkinter.Canvas(root, width=600, height=400)
cvs.pack()
line1_id = cvs.create_line(100, 100, 200, 200)
img = tkinter.PhotoImage(file="./bee.gif")
bee1_id = cvs.create_image(200, 100, image=img)

y = 100

def on_time():
    global y
    y += 1
    cvs.coords(bee1_id, 200, y)
    root.after(50, on_time)

root.after(50, on_time)


root.mainloop()