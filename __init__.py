from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
cwd = os.getcwd()
print cwd
sys.stdout.flush()
def configure(app):
    app.debug = True
    hook_routes()
    configuredb(app)

def configuredb(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\database.db'

def hook_routes():
    from hackkings import views

app = Flask(__name__)

configure(app)
db = SQLAlchemy(app)
import hackkings.models
db.create_all()