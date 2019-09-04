
import tkinter
import random

# _map_data = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]


_map_data = [
    [0, 2, 0, 4],
    [2, 2, 8, 8],
    [0, 0, 0, 2],
    [0, 2, 2, 0]
]

# [2, 4, 0, 0],
# [4, 16, 0, 0],
# [2, 0, 0, 0],
# [4, 0, 0, 0]


def _left_move_number(line):
    '''如果line = [0, 2, 0, 2]
       结果是: line = [2, 2, 0, 0]
    '''
    for _ in range(3):
        for i in range(3):  # i代表当前数的索引
            if line[i] == 0:
                line[i] = line[i+1]  # 后面的一个数前移一个位置
                line[i+1] = 0


def _left_merge_number(line):
    '''如果line = [2, 2, 8, 8]
    结果line = [4, 0, 16, 0]'''
    for i in range(3):
        if line[i] == line[i+1]:
            line[i] *= 2
            line[i+1] = 0


def left():
    '''向左移地图
    如果
        _map_data = [
            [0, 2, 0, 4],
            [2, 2, 8, 8],
            [0, 0, 0, 2],
            [0, 2, 2, 0]
        ]
    结果:
        _map_data = [
            [2, 4, 0, 0],
            [4, 16, 0, 0],
            [2, 0, 0, 0],
            [4, 0, 0, 0]
        ]
    '''
    for line in _map_data:  # line 绑定一行
        _left_move_number(line)  # 左移
        _left_merge_number(line)  # 合并(可能有空缺)
        _left_move_number(line)  # 左移

def right():
    for line in _map_data:
        line.reverse()
    left()
    for line in _map_data:
        line.reverse()


def up():
    line = [0, 0, 0, 0]  # 先初始化一行，准备放入数据
    for col in range(4):  # 先取出每一列
        for row in range(4):
            line[row] = _map_data[row][col]

        _left_move_number(line)
        _left_merge_number(line)
        _left_move_number(line)

        for row in range(4):
            _map_data[row][col] = line[row]


def down():
    _map_data.reverse()
    up()  # 上滑
    _map_data.reverse()

def reset():
    '''将数据全部清零'''
    for line in _map_data:
        for i in range(4):
            line[i] = 0
    fill2()
    fill2()  

def get_space_count():
    """获取没有数字的方格的数量,如果数量为0则说有无法填充新数据，游戏即将结束
    """
    count = 0
    for r in _map_data:
        count += r.count(0)
    return count

def fill2():
    '''填充2到空位置，如果填度成功返回True,如果已满，则返回False'''
    blank_count = get_space_count()  # 得到地图上空白位置的个数
    if 0 == blank_count:
        return False
    # 生成随机位置, 如，当只有四个空时，则生成0~3的数，代表自左至右，自上而下的空位置
    pos = random.randrange(0, blank_count)
    offset = 0
    for row in _map_data:   # row为行row
        for col in range(4):  # col 为列，column
            if 0 == row[col]:
                if offset == pos:
                    # 把2填充到第row行，第col列的位置，返回True
                    row[col] = 2
                    return True
                offset += 1


def main():
    root = tkinter.Tk()

    def update_ui():
        for r in range(4):
            for c in range(4):
                number = _map_data[r][c]  # 拿到数字
                number = str(number) if number else ""  # 转为字符串
                map_labels[r][c].config(text=number)

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
        reset()
        update_ui()

    restart_button = tkinter.Button(root, text='重新开始', font=("黑体", 16, "bold"),
                            bg="#8f7a66", fg="#f9f6f2", command=reset_game)
    restart_button.grid(row=4, column=3, padx=5, pady=5)

    def onKeyDown(event):
        if event.keysym == 'Left':
            left()
            fill2()
        elif event.keysym == 'Right':
            right()
            fill2()
        elif event.keysym == 'Up':
            up()
            fill2()
        elif event.keysym == 'Down':
            down()
            fill2()
        update_ui()

    root.bind('<Key>', onKeyDown)  # 注册按键事件
    reset_game()
    root.mainloop()


main()
