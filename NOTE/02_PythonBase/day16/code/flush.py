# flush.py


fw = open("myflush.txt", 'w')

fw.write("hello")
fw.flush()  # 立即将缓冲区的内容写入磁盘(即使缓冲区未满
            # 也会进行一次磁盘的IO操作)

while True:
    pass
# fw.write("hello")
# fw.write(' world!')
# import time
# while True:
#     fw.write("1234567890")
#     time.sleep

fw.close()