from flask_wtf import Form
from wtforms import TextField, PasswordField, RadioField, SubmitField
from hackkings.models import User
from wtforms.validators import DataRequired, ValidationError

class SignupForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = TextField('Email Address', validators=[DataRequired()])
    name = TextField('Name', validators=[DataRequired()])
    role = RadioField('What\'s your role?', coerce=int, validators=[DataRequired()])
    submit = SubmitField()

    def validate_username(form, field):
        if len(field.data) == 0:
            raise ValidationError('That\'s not a good username!')
        if User.find_by_username(field.data):
            raise ValidationError('That username has already been taken')

    def validate_email(form, field):
        if User.find_by_email(field.data):
            raise ValidationError('That email address has already been registered to an account')

