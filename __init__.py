from flask import Flask, redirect, request
from flask.ext.sqlalchemy import SQLAlchemy
from hackkings.constants import SITENAME
from flask_login import LoginManager, current_user

import os
import sys

login_manager = LoginManager()

def configure_app(app):
    from hackkings.models import User
    app.debug = True
    app.config['SECRET_KEY'] = 'hello'
    app.config['UPLOADED_PHOTOS_DEST'] = 'hackkings/static/uploads'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(userid):
        return User.find(userid)
    @login_manager.unauthorized_handler
    def redirect_login():
        return redirect('/login')



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

    @app.context_processor
    def inject_path():
        return dict(PATH=request.path)

    @app.context_processor
    def inject_authenticated():
        return dict(AUTHENTICATED=current_user.is_authenticated())

def hook_routes():
    from hackkings import views

app = Flask(__name__)

db = SQLAlchemy(app)
configure_db(app)
configure_jinja(app)
import hackkings.models

db.drop_all()
db.create_all()
import dummydata

configure_app(app)

hook_routes()
