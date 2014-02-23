from flask import render_template, flash
from hackkings import app, db
from flask_login import current_user, login_required
from hackkings.forms import SettingsForm
from hackkings.models import Skill
from hackkings.models import User

VALID_FIELDS = ['name', 'email', 'password', 'avatar', 'bio', 'code_academy_username', 'skills']

@app.route('/profile/settings', methods=['GET', 'POST'])
@login_required
def settings():
    
    user = User.find(current_user.id)
    settings_form = SettingsForm()

    #setattr(current_user, key, getattr(settings_form, key))
    print dir(settings_form.skills)
    print settings_form.skills.data
    settings_form.skills.choices = [(skill.id, skill.name) for skill in Skill.query.all()]
    settings_form.skills.data = [skill.id for skill in user.skills]

    if settings_form.validate_on_submit():
        if settings_form.name.data:
            current_user.set_name(settings_form.name.data)
        if settings_form.email.data:
            current_user.set_email(settings_form.email.data)
        if settings_form.bio.data:
            current_user.set_bio(settings_form.bio.data)
        if settings_form.code_academy_username.data:
            current_user.set_code_academy_username(settings_form.code_academy_username.data)

        existing_skill_ids = [skill.id for skill in user.skills]
        if settings_form.skills.data and settings_form.skills.data != existing_skill_ids:
            print 'editing skills'
            for skill_id in settings_form.skills.data:
                if skill_id not in existing_skill_ids:
                    user.add_skill_id(skill_id)
            for skill_id in existing_skill_ids:
                if skill_id not in settings_form.skills.data:
                    user.remove_skill_id(skill_id)
            
        flash('Settings changed')

    settings_form.name.data = user.name
    settings_form.email.data = user.email
    settings_form.avatar.data = user.avatar
    settings_form.bio.data = user.bio
    settings_form.code_academy_username.data = user.code_academy_username



    return render_template('settings.html', settings_form=settings_form, skills=Skill.query.all())
    
