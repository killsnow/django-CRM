import mysql.connector

# 使用config将数据库连接信息存储

config = {
    'user': 'root',
    'password': 'password',
    'host': '192.168.1.2',
}

# 连接到指定的数据库
dataBase=mysql.connector.connect(**config)

# 创建一个游标对象
cursorObject = dataBase.cursor()

# 创建一个数据库
cursorObject.execute('CREATE DATABASE elderco')

print("All Done!")