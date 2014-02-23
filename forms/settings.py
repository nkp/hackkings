from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from hackkings.models import User
from flask_login import current_user

class SettingsForm(Form):
    name = TextField('Name')
    email = TextField('Email')
    password = PasswordField('Password')
    avatar = TextField('Avatar')
    bio = TextAreaField('Tell us about yourself!')
    code_academy_username = TextField('Code academy username')
    skills = SelectMultipleField('Skills', coerce=int)
    remember_me = BooleanField('Remember me?')
    submit = SubmitField()

    def validate_bio(form, field):
        if len(field.data) > 5000:
            return ValidationError('Biography too long')

    def validate_username(form, field):
        u = User.find_by_username(field.data)
        if u and u != current_user:
            raise ValidationError('That username has already been taken')

    def validate_email(form, field):
        u = User.find_by_email(field.data)
        if u and u != current_user:
            raise ValidationError('That email address has already been registered to an account')

    
