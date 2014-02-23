from flask_login import logout_user, current_user

@app.route('/logout', methods=('POST'))
def logout():
    if current_user.is_authenticated():
        logout_user(current_user)
    return redirect('/')

