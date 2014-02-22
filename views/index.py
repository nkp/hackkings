from flask import render_template, current_app

from hackkings import app

@app.route('/')
def index():
    return render_template('index.html')

