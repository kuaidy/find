# encoding: utf-8 
#!/usr/bin/python3
import pymysql

class MysqlHelp:
	#构造函数
	def __init__(self):
		try:
			# 打开数据库连接
			self.conn=pymysql.connect("localhost","root","Kuai1227.","find")
			self.cursor=self.conn.cursor()
		except:
			print("连接错误") 

	def ExecuteQuery(self,sql):
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			self.conn.close()
		except:
			print("执行错误") 

	def testdb(self,sql):
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		self.conn.commit()
		self.conn.close()
		return rows
sql="select * from user"
mysqldb=MysqlHelp()
datas=mysqldb.testdb(sql)
users=[]
for data in datas:
	users.append(data)

for user in users:
	print(user[2])

