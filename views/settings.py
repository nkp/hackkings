from flask import render_template, flash
from hackkings import app
from flask_login import current_user, login_required
from hackkings.forms import SettingsForm
from hackkings.models import Skill

VALID_FIELDS = ['name', 'email', 'password', 'avatar', 'bio', 'code_academy_username', 'skills']

@app.route('/profile/settings', methods=['GET', 'POST'])
@login_required
def settings():
    
    settings_form = SettingsForm()

    #setattr(current_user, key, getattr(settings_form, key))
    print dir(settings_form.skills)
    settings_form.skills.data = [skill.id for skill in current_user.skills]
    print settings_form.skills.data
    settings_form.skills.choices = [(skill.id, skill.name) for skill in Skill.query.all()]

    if settings_form.validate_on_submit():
        for key in VALID_FIELDS:
            setattr(current_user, key, getattr(settings_form, key))
        flash('Settings changed')

    return render_template('settings.html', settings_form=settings_form, skills=Skill.query.all())
    
