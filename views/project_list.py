from flask import render_template, current_app
from flask_login import current_user, login_required
from hackkings import app
from hackkings.models import Project

@app.route('/projects')
@login_required
def project_list():
    project_list = Project.get_all_current_projects()
    
    return render_template('projects.html', project_list = project_list)
