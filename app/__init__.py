import os
from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.user import *
from app.index import *
from app.products import *
from app.publish import *
from setting import config

def create_app(config_name=None):
	if config_name is None:
		config_name=os.getenv('FLASK_CONFIG','development')

	app=Flask(__name__)
	app.config.from_object(config[config_name])

	register_extensions(app)
	register_blueprints(app)

	return app

def register_blueprints(app):
	app.register_blueprint(bp_index)
	app.register_blueprint(bp_user)
	app.register_blueprint(bp_product)
	app.register_blueprint(bp_publish)

def register_extensions(app):
	db.init_app(app)
