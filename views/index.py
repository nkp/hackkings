from flask import render_template, current_app
from flask_login import current_user
from hackkings import app
from hackkings.constants import ROLES
from hackkings.models import Project

@app.route('/')
def index():
    if current_user.is_authenticated():
        return landing()
    return render_template('index.html')

def landing():
    landing_page_data = {}

    def get_suggestions():
        pending_projects = Project.get_all_pending_projects()
        skills = current_user.get_skills()
        suggestions = []
        skills_needed = []
        for p in pending_projects:
            skills_needed = p.get_skills()
            for s in skills:
                if s in skills_needed:
                    suggestions.append(p)
                    break
        return suggestions

    if current_user.role == ROLES.DEVELOPER:
        landing_page_data = { 'role' : current_user.role,
                              'ongoing_projects': current_user.get_ongoing_projects(),
                              'completed_projects': current_user.get_completed_projects(),
                              'suggested_projects': get_suggestions() }
    elif current_user.role == ROLES.PROPOSER:
        landing_page_data = { 'role' : current_user.role,
                              'ongoing_proposals': current_user.get_ongoing_proposals(),
                              'pending_proposals': current_user.get_pending_proposals(),
                              'completed_proposals': current_user.get_completed_proposals() }
    else:
        abort(400)

    return render_template('landing.html', **landing_page_data)