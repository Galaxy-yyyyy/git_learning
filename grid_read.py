# 获取grid方案　存放到数据中的文件
from pymongo import MongoClient

import gridfs

conn = MongoClient('localhost',27017)

db = conn.grid 

# 获取gridfs对象
fs = gridfs.GridFS(db)

files = fs.find()

# 分别取每一个文件
for file in files:
    # print(file.filename)　　
    if file.filename == 'img.png':
        with open(file.filename,'wb') as f:
            # data = file.read()
            # f.write(data)
            # # 从数据库读取内容
            
                try:
                    while 1:
                        data = file.read()
                        if not data:
                            break
                         # 写入到本地
                        f.write(data)
                except:
                    print('文件写入完毕')
                    break
                else:
                    print('文件读写无差错')

conn.close()

# with open('aa.txt') as f:
#     f.read()
