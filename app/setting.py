#encoding:utf-8

import os
import sys
import pymysql

basedir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Kuai1227.@localhost:3306/find?charset=utf8'


config={
    'development':DevelopmentConfig
}

