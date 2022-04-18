from flask import Blueprint,render_template

bp_publish=Blueprint('publish',__name__,url_prefix='/publish')


@bp_publish.route('')
def home():
	return render_template('publish.html')
