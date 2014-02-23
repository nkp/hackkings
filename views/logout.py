from hackkings import app
from flask_login import logout_user, current_user, redirect

@app.route('/logout', methods=['POST'])
def logout():
    if current_user.is_authenticated():
        logout_user()
    return redirect('/')

