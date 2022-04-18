from flask import Blueprint,render_template,request

import sqldbhelp

bp_user=Blueprint('user',__name__,url_prefix='/user')

@bp_user.route('/signin',methods=('GET','POST'))
def signin():
	if(request.method=="POST"):
		username=request.form["username"]
		password=request.form["password"]
		strsql="select * from user where username ='"+username+"' and password = '"+password+"'"
		mysqldb=sqldbhelp.MysqlHelp()
		mysqldb.ExecuteQuery(strsql)	
	return render_template('signin.html')

@bp_user.route('/signup',methods=('GET','POST'))
def signup():
	if(request.method=="POST"):
		username=request.form["username"]
		password=request.form["password"]
		conformpwd=request.form["conformpwd"]
		if(len(username)!=0 and len(password)!=0 and len(conformpwd)!=0):
			if(password==conformpwd):
				strsql="insert into user (username,password) values ('"+username+"','"+password+"')"
				mysqldb=sqldbhelp.MysqlHelp()
				mysqldb.ExecuteQuery(strsql)
	return render_template("signup.html")


