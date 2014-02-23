from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class ProjectForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    description = TextField('Description', validators=[DataRequired()])
    time_estimate = TextField('Estimated Time', validators=[DataRequired()])
    difficulty = TextField('Difficulty', validators=[DataRequired()])
    submit = SubmitField()