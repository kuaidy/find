#encoding:utf-8
from flask import Blueprint,render_template
from extensions import db
from models import Product,LikeProducts

bp_index=Blueprint('index',__name__,url_prefix='')

@bp_index.route('/')
def home():
	likeproduct=session.query(LikeProducts.productid,func.count('*').label('likecount')).group_by(LikeProducts.productid).subquery())
	products=session.query(Product, likeproduct.c.likecount).outerjoin(likeproduct, Product.id==LikeProducts.productid).order_by(Product.date.desc()).all()
	products=Product.query.order_by(Product.date.desc())
	likecount=LikeProducts.query.filter()
	return render_template('index.html',products=products)
