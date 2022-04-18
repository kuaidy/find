#encoding:utf-8
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

	def QueryAll(self,sql):
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		self.conn.commit()
		self.conn.close()
		return rows

