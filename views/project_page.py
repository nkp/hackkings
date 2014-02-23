from flask import render_template, current_app, abort
from hackkings import app
from hackkings.models import Project
from flask_login import current_user
from hackkings.constants import STATES

@app.route('/project/<int:id>/apply')
def project_apply():
    if id == None:
        abort(404)         

    project = Project.find(id)
    if project == None:
        abort(404)
    

    new_thread = MessageThread.create([project.proposer, current_user])
    initial_message = Message.create(new_thread, current_user, 'Hi! I would like to work on your project!')

    project.add_developer(current_user)


@app.route('/project/<int:id>')
def project_page(id=None):
    if id == None:
        abort(404)         
    project = Project.find(id)
    if project == None:
        abort(404)
    
    project_data = { 'name': project.name,
                     'id': project.id,
                     'proposer': project.proposer,
                     'difficulty': project.difficulty,
                     'time_estimate': project.time_estimate,
                     'description': project.description,
                     'attachments': project.get_attachments(),
                     'skills_needed': project.get_skills(),
                     'currently_working': project.get_current_developers() }

    return render_template('project.html', project=project_data)
