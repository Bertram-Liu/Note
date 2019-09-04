# tkinter_helloworld.py

#   1. 导入Tkinter模块
import tkinter

#   2. 创建一个顶层的窗口对象,用于容纳整个GUI应用
root = tkinter.Tk()


#   3. 在顶层窗口对象上(或其中)构建所有的GUI组件
label = tkinter.Label(root, text="hello world")
#   4. 通过底层的应用代码将这些GUI 组件连接起来

label.pack()  # 放入 root窗口中

#   5. 进入主事件循环(mainloop)
root.mainloop()
