from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from hackkings.models import User

class SettingsForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    bio = TextField('Tell us about yourself!')
    code_academy_username = TextField('Code academy username')
    skills = SelectField('Skills')
    remember_me = BooleanField('Remember me?')
    submit = SubmitField()

    def validate_identifier(form, field):
        print field.data
        if not User.find_by_identifier(field.data):
            return ValidationError('No user found')

        
