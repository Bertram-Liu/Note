
import tkinter

def main():
    root = tkinter.Tk()

    # ... 在此处创建主窗口及内部的Label
    map_labels = []
    for r in range(4):  # r代表行
        row = []
        for c in range(4):  # c 代表列
            label = tkinter.Label(root, text='0',
                    font=('黑体', 30, 'bold'),
                    width=4, height=2, 
                    bg="#cdc1b4",
                    fg="#776e65")
            label.grid(row=r, column=c, padx=5, pady=5)
            row.append(label)
        map_labels.append(row)

    # 设置显示分数的Lable
    label = tkinter.Label(root, text='分数', font=("黑体", 30, "bold"),
                  bg="#bbada0", fg="#eee4da")
    label.grid(row=4, column=0, padx=5, pady=5)
    label_score = tkinter.Label(root, text='0', font=("黑体", 30, "bold"),
                        bg="#bbada0", fg="#ffffff")
    label_score.grid(row=4, columnspan=2, column=1, padx=5, pady=5)

    # 以下设置重新开始按钮
    def reset_game():
        print("重新开始")
        pass
        # reset()
        # update_ui()

    restart_button = tkinter.Button(root, text='重新开始', font=("黑体", 16, "bold"),
                            bg="#8f7a66", fg="#f9f6f2", command=reset_game)
    restart_button.grid(row=4, column=3, padx=5, pady=5)


    root.mainloop()
    print("程序退出")



main()
