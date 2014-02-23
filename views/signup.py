from flask import render_template, current_app

from hackkings import app
from hackkings.constants import ROLES
from hackkings.forms import SignupForm

@app.route('/signup')
@app.route('/signup/<role>')
def signup(role=None):
    print 'signup'
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        User.create(signup_form.username, signup

    role = role.lower().strip()
    if role == 'developer':
        return render_template('signup.developer.html', signup_form = signup_form)
    elif role == 'proposer':
        return render_template('signup.proposer.html', signup_form = signup_form)
    else:
        return render_template('signup.html', signup_form = signup_form)
