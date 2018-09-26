# 小文件存储方案
# 直接转化为二进制格式插入到数据库中

from pymongo import MongoClient
import gridfs
import bson.binary

conn = MongoClient('localhost',27017)

db = conn.image

myset = db.MM

# # 存储图片
# f = open('img.png','rb')
# # 将图片内容转化为可存储的二进制格式
# content = bson.binary.Binary(f.read())

# # 插入到文档
# myset.insert({'filename':'img.png','data':content})

#提取图片
img1 = myset.find_one({'filename':'img.png'})
# 将内容写入到本地
with open('img.png','wb') as f:
    f.write(img1['data'])



conn.close()

