#   1. 写程序,实现复制文件的功能
#     要求:
#       1. 要考虑关闭文件的问题
#       2. 要考虑超大文件的问题
#       3. 要能复制二进制文件

def copy(src_file, dst_file):
    '''src_file 源文件
    dst_file 目标文件'''
    # 以下实现复制
    try:
        fr = open(src_file, 'rb')
        try:
            fw = open(dst_file, 'wb')
            try:
                # 此处开始复制
                while True:
                    b = fr.read(4096)
                    if not b:  # 到达文件尾
                        break
                    fw.write(b)
            finally:
                fw.close()
        finally:
            fr.close()
    except OSError:
        print("复制失败!")

src = input("请输入源文件名: ")
dst = input('请输入目标文件名: ')
copy(src, dst)





