from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from hackkings.constants import SITENAME

import os
import sys

def configure(app):
    app.debug = True
    hook_routes()
    configuredb(app)

def configuredb(app):
    path = ''
    if os.name == 'nt':
        path = 'sqlite:///C:\\database.db'
    else:
        path = 'sqlite:////tmp/database.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = path


def configure_jinja(app):
    @app.context_processor
    def inject_sitename():
        return {'SITENAME':SITENAME}

def hook_routes():
    from hackkings import views

app = Flask(__name__)

configure(app)

db = SQLAlchemy(app)
import hackkings.models

db.create_all()
import dummydata
