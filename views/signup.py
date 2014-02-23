from flask import render_template, current_app

from hackkings import app
from hackkings.constants import ROLES

@app.route('/signup')
@app.route('/signup/<role>')
def signup(role=None):
    print 'signup'
    role = role.lower().strip()
    if role == 'developer':
        return render_template('signup.developer.html')
    elif role == 'proposer':
        return render_template('signup.proposer.html')
    else:
        return render_template('signup.html')
