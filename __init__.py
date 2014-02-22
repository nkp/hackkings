from flask import Flask

def configure(app):
    app.debug = True
    hook_routes()


def hook_routes():
    from hackkings import views

app = Flask(__name__)

configure(app)

