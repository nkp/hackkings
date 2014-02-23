from flask import render_template, current_app
from flask_login import current_user, login_required
from hackkings import app
from hackkings.forms import ProjectForm

@login_required
@app.route('/project/new')
def project_signup():
    print 'signup'
    signup_form = ProjectForm()
    if current_user.is_proposer():
        if signup_form.validate_on_submit():
            Project.create(signup_form.name.data, current_user.id, signup_form.description.data, 
                        signup_form.time_estimate.data, signup_form.difficulty.data)
            return 201, 'Success'
    else
        return 401, 'Failure must be proposer'
    return render_template('project.signup.html', signup_form = signup_form)

