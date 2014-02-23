from flask_wtf import Form
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ProjectForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    time_estimate = TextField('Approximate Duration (hours)', validators=[DataRequired()])
    difficulty = TextField('Difficulty', validators=[DataRequired()])
    submit = SubmitField()