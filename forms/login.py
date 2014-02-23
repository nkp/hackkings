from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from hackkings.models import User

class LoginForm(Form):
    identifier = TextField('Username or email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?')
    submit = SubmitField()

    def validate_identifier(form, field):
        print field.data
        if not User.find_by_identifier(field.data):
            return ValidationError('No user found')

        
