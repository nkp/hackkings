from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

def configure(app):
    app.debug = True
    hook_routes()
    configuredb(app)

def configuredb(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////./test.db'

def hook_routes():
    from hackkings import views

app = Flask(__name__)

configure(app)
db = SQLAlchemy(app)