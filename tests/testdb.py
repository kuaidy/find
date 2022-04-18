#!/usr/bin/python3
# encoding: utf-8 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","Kuai1227.","find" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("select * from product")
 
# 使用 fetchone() 方法获取单条数据.
dataone = cursor.fetchone()

dataall=cursor.fetchall()
 
print ("one",dataone[1])
print ("all",dataall)
 
# 关闭数据库连接
db.close()
