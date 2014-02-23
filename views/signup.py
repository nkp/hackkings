from flask import render_template, current_app

from hackkings import app
from hackkings.constants import ROLES
from hackkings.forms import SignupForm

@app.route('/signup')
@app.route('/signup/<role>')
def signup(role=None, methods=('GET', 'POST')):
    print 'signup'
    signup_form = SignupForm()
    signup_form.role.choices = [(ROLES.DEVELOPER, 'Developer'), (ROLES.PROPOSER, 'Proposer')]

    if signup_form.validate_on_submit():
        User.create(signup_form.username.data, signup_form.email.data, 
                    signup_form.password.data, signup_form.role.data)
        return 201, 'Success'
    if not role:
        return render_template('signup.html', signup_form = signup_form)
    role = role.lower().strip()
    if role == 'developer':
        return render_template('signup.developer.html', signup_form = signup_form)
    elif role == 'proposer':
        return render_template('signup.proposer.html', signup_form = signup_form)
