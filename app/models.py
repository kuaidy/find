#encoding:utf=8
from extensions import db

class Product(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(999))	
	description=db.Column(db.String(9999))
	userid=db.Column(db.Integer)	
	date=db.Column(db.DateTime)
	time=db.Column(db.DateTime)	
	classid=db.Column(db.Integer)
	bak=db.Column(db.String(999))	
	
class Likeproducts(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer)	
	productid=db.Column(db.Integer)

class Comments(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	productid=db.Column(db.Integer)
	fromuser=db.Column(db.Integer)
	touser=db.Column(db.Integer)
	content=db.Column(db.Text)
	date=db.Column(db.DateTime)
	bak=db.Column(db.Text)

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(50))
	password=db.Column(db.String(50))
	phone=db.Column(db.String(11))
	email=db.Column(db.String(50))
	status=db.Column(db.String(2))
	bak=db.Column(db.String(50))