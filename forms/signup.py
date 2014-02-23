from flask_wtf import Form
from wtforms import TextField, PasswordField, RadioField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = TextField('email', validators=[DataRequired()])
    name = TextField('name', validators=[DataRequired()])
    role = RadioField('role')
    submit = SubmitField()
