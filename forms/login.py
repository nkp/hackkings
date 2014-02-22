from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    name = TextField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')