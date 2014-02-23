from flask import render_template, current_app, redirect, abort

from hackkings import app
from hackkings.constants import ROLES
from hackkings.forms import LoginForm
from flask_login import login_user
from hackkings.models import User


@app.route('/login', methods=('GET', 'POST'))
def login():
    print 'login'
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.find_by_identifier(login_form.identifier.data)
        if not user:
            abort(404) # User not found
        if user.check_password(login_form.password.data):
            login_user(user)
        return redirect('/')
    return render_template('login.html', login_form=login_form)
