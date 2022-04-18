#encoding:utf-8
import time
from flask import Blueprint,render_template,request
from extensions import db
from models import Product,Likeproducts,Comments,User

bp_product=Blueprint('product',__name__,url_prefix='/product')


@bp_product.route('/<int:post_id>')
def GetProduct(post_id):
	product=Product.query.get(post_id)
	productlist=Product.query.filter_by(date=product.date)
	productdate=str(product.date).split()[0]

	users=[]
	likecount=0
	likeinfo=Likeproducts.query.filter_by(productid=post_id)
	for likeitem in likeinfo:
		likecount=likecount+1
		userinfo=User.query.filter_by(id=likeitem.userid)
		users.append(userinfo)
		
	return render_template('content.html',product=product,productlist=productlist,productdate=productdate,likecount=likecount,users=users)


