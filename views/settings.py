from hackkings import app
from flask_login import current_user
from hackkings.forms import SettingsForm
from hackings.models import Skill

VALID_FIELDS = ['name', 'email', 'password', 'avatar', 'bio', 'code_academy_username', 'skills']

@app.route('/profile/settings', methods=['GET', 'POST'])
@login_required
def settings():
    
    settings_form = SettingsForm()

    if settings_form.validate_on_submit():
        for key in VALID_FIELDS:
            setattr(current_user, key, getattr(settings_form, key))
        flash('Settings changed')

    return render_template('settings.html', settings_form=settings_form, skills=Skill.query.all())
    
