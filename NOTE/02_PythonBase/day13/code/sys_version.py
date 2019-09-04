

import sys
print("current Version is ", sys.version)

# 在此处能知道我这个程序运行在windows还是Linux上吗?
if sys.platform == 'linux':
    print('run in linux')
elif sys.platform == 'win32':
    print('run in windows')
elif sys.platform == 'darwin':
    print('run in MAC OS X')
    
