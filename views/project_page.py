from flask import render_template, current_app, abort, redirect
from hackkings import app
from hackkings.models import Project, MessageThread, Message
from flask_login import current_user
from hackkings.constants import STATES

@app.route('/project/<int:id>/apply')
def project_apply(id=None):
    if id == None:
        abort(404)         

    project = Project.find(id)
    if project == None:
        abort(404)

    if current_user in project.developers.all():
        abort(400)

    new_thread = MessageThread.create([project.proposer, current_user])
    initial_message = Message.create(new_thread, current_user, 'Hi! I would like to work on your project!')

    project.add_developer(current_user)

    return redirect('/project/%d' % id) 

@app.route('/project/<int:id>/unapply')
def project_unapply(id=None):
    if id == None:
        abort(404)         

    project = Project.find(id)
    if project == None:
        abort(404)

    if current_user not in project.developers.all():
        abort(400)

    project.remove_developer(current_user)

    return redirect('/project/%d' % id) 


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

    return render_template('project.html', project=project_data, 
            current_user=current_user)
