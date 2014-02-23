from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from hackkings.constants import SITENAME
from flask_login import LoginManager

import os
import sys

login_manager = LoginManager()

def configure_app(app):
    from hackkings.models import User
    app.debug = True
    app.config['SECRET_KEY'] = 'hello'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(userid):
        return User.find(userid)


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
configure_db(app)
import hackkings.models

db.drop_all()
db.create_all()
import dummydata

configure_app(app)

hook_routes()
