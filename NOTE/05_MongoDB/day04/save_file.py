from pymongo import MongoClient
import bson.binary 

conn = MongoClient('localhost',27017)
db = conn.image 
myset = db.mm  

#　存储图片
# f = open('test.jpg','rb')
# data = f.read() 

# # 转换ｂｓｏｎ格式
# content = bson.binary.Binary(data)

# myset.insert_one({'filename':'mm.jpg','data':content})

#　文件提取
img = myset.find_one({'filename':'mm.jpg'})

#　将ｄａｔａ写入新文件
with open('mm.jpg','wb') as f:
    f.write(img['data'])

conn.close()
