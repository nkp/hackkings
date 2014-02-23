from flask import render_template, current_app, abort
from hackkings import app, db
from hackkings.models import User
from hackkings.constants import ROLES
from flask_login import current_user


@app.route('/profile')
@app.route('/profile/<int:id>')
def profile_page(id=None):
    if id == None:
        user = current_user
    else:
        user = User.find(id)
    if user == None:
        abort(404)

    profile_data = {}
    if user.role == ROLES.DEVELOPER:
        profile_data = { 'ongoing_projects': user.get_ongoing_projects(),
                         'completed_projects': user.get_completed_projects(),
                         'username': user.username,
                         'avatar': user.avatar,
                         'description': user.bio,
                         'skills': user.get_skills(),
                         'role' : user.role,
                         'codeacademy_badges': [] } 
    elif user.role == ROLES.PROPOSER:
        profile_data = { 'ongoing_proposals': user.get_ongoing_proposals(),
                         'pending_proposals': user.get_pending_proposals(),
                         'completed_proposals': user.get_completed_proposals(),
                         'name': user.name,
                         'description': user.bio,
                         'avatar': user.avatar,
                         'role' : user.role}
    else:
        abort(400)

    print current_user.role

    return render_template('profile.html', user=user, **profile_data)
