from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from hackkings.constants import SITENAME

def configure(app):
    app.debug = True
    hook_routes()
    configuredb(app)

def configuredb(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

def configure_jinja(app):
    @app.context_processor
    def inject_sitename():
        return {'SITENAME':SITENAME}

def hook_routes():
    from hackkings import views

app = Flask(__name__)

configure(app)
db = SQLAlchemy(app)
