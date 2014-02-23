from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    identifier = TextField('Username or email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me?')
    submit = SubmitField()
