from test import * 
import threading
import time 

jobs = []
t = time.time()
for i in range(10):
    # th = threading.Thread(target = count,args=(1,1))
    th = threading.Thread(target = io)
    jobs.append(th)
    th.start()
for i in jobs:
    i.join()
print("Thread IO:",time.time() - t)
