import re 
import sys 

port = sys.argv[1]

f = open('1.txt')

#　找到端口所在段落
while True:
    data = ''
    for line in f:
        if line != '\n':
            data += line 
        else:
            break
    
    if not data:
        print("No PORT")
        break
    
    #　获取每一段首单词
    try:
        PORT = re.match(r'\S+',data).group()
    except Exception:
        continue
   
    if PORT == port:
        # pattern = r'[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}'
        pattern = r'([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknown'
        address = re.search(pattern,data).group()
        print(address)
        break


f.close()


