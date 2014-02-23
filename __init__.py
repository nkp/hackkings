from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from hackkings.constants import SITENAME

import os
import sys

def configure_app(app):
    app.debug = True
    app.config['SECRET_KEY'] = 'hello'
    hook_routes()

def configure_db(app):
    path = ''
    if os.name == 'nt':
        path = 'sqlite:///C:\\database.db'
    else:
        path = 'sqlite:////tmp/database.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = path


def configure_jinja(app):
    @app.context_processor
    def inject_sitename():
        return dict(SITENAME=SITENAME)

def hook_routes():
    from hackkings import views

app = Flask(__name__)

db = SQLAlchemy(app)
import hackkings.models
configure_db(app)

db.drop_all()
db.create_all()
import dummydata

configure_app(app)
