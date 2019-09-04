# event1.py

# 此示例示意tkinter事件

import tkinter
root = tkinter.Tk()

def mouseDown(e):
    print("有鼠标按键按下 x:", e.x,
                       'y:', e.y, "按键:", e.num)

def mouseUp(e):
    print("有鼠标按键抬起")

# root.bind('<Button-1>', mouseDown)
root.bind('<Button>', mouseDown)
root.bind('<ButtonRelease-1>', mouseUp)

def keyDown(e):
    print("有键盘按键接下:", e.keysym)

def keyUp(e):
    print("有键盘抬起:", e.keysym)

root.bind('<Key>', keyDown)
root.bind('<KeyRelease>', keyUp)


root.mainloop()


