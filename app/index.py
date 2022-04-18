#encoding:utf-8
from flask import Blueprint,render_template
from extensions import db
from models import Product,Likeproducts

bp_index=Blueprint('index',__name__,url_prefix='')

@bp_index.route('/')
def home():
	#products=db.session.query(Product).outerjoin(Likeproducts, Product.id==Likeproducts.productid).order_by(Product.date.desc()).all()
	productitems=[]
	products=db.session.query(Product).order_by(Product.date.desc())
	for product in products:
		likecount=db.session.query(Likeproducts).filter(Likeproducts.productid==product.id).count()
		productitems.append({'id':product.id,'title':product.title,'description':product.description,'likecount':likecount})
	return render_template('index.html',products=productitems)
