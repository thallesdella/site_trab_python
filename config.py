import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DB_HOST = '192.168.0.2'
	DB_USER = 'root'
	DB_PASS = ''
	DB_DBSA = 'thallesdella'
	
	BASE = 'http://localhost:5000'
	
	SITE_NAME = 'Trab. Programação'
	SITE_DESC = 'Site desenvolvido como trabalho do curso de Programação em Python 2018.2'
	SITE_FONT_FAMILY = 'Open Sans'
	SITE_FONT_SIZE = '300,400,600,700,800'
	
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_DBSA)
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	
