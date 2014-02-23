from flask import render_template, current_app
from flask_login import current_user
from hackkings import app

@app.route('/')
def index():
    if current_user.is_authenticated():
        return render_template('landing.html')
    return render_template('index.html')

