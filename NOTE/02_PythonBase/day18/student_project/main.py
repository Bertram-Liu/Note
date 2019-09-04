# file: main.py

from menu import show_menu
from student_info import *

def main():
    infos = []  # 此列表用来保存学生信息的数据
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            delete_student(infos)  # 删除学生
        elif s == '4':
            modify_student_score(infos)  # 修改学生成绩
        elif s == '5':
            print_student_by_score_desc(infos)  # desc降序
        elif s == '6':
            print_student_by_score_asc(infos)  # asc升序
        elif s == '7':
            print_student_by_age_desc(infos)
        elif s == '8':
            print_student_by_age_asc(infos)
        elif s == '9':
            infos = read_from_file()  # 从文件中读取数据
        elif s == '10':
            save_to_file(infos)  # 保存到文件
        elif s == 'q':
            break
main()
