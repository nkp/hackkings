from flask import render_template, current_app

from hackkings import app
from hackkings.constants import ROLES

@app.route('/signup')
@app.route('/signup/<role>')
def signup(role=None):
    if role == ROLES.DEVELOPER:
        return render_template('signup.developer.html')
    elif role == ROLES.PROPOSER:
        return render_template('signup.proposer.html')
    else:
        return render_template('signup.html')
