from flask import render_template, current_app, abort, redirect
from flask_login import current_user, login_required
from hackkings import app
from hackkings.forms import ProjectForm
from hackkings.models import Project

@app.route('/project/new', methods=('GET', 'POST'))
@login_required
def project_signup():
    print 'signup'
    signup_form = ProjectForm()
    if current_user.is_proposer():
        if signup_form.validate_on_submit():
            new_project = Project.create(signup_form.name.data, current_user, signup_form.description.data, 
                        signup_form.time_estimate.data, signup_form.difficulty.data)
            return redirect('/project/%d' % new_project.id)
    else:
        abort(401)
    return render_template('project.signup.html', signup_form = signup_form)

