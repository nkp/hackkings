from flask import render_template, current_app, abort
from hackkings import app, db
from hackkings.models import User
from hackkings.constants import ROLES

@app.route('/user/<int:id>')
def profile_page(id=None):
    if id == None:
        abort(404)
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
                         'codeacademy_badges': [] } 
    elif user.role == PROPOSER:
        profile_data = { 'ongoing_proposals': user.get_ongoing_proposals(),
                         'pending_proposals': user.get_pending_proposals(),
                         'completed_proposals': user.get_completed_proposals(),
                         'name': user.name,
                         'description': user.bio,
                         'avatar': user.avatar }
    else:
        abort(400)

    return render_template('profile.html', **profile_data)
