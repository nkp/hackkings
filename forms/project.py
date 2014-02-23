from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class ProjectForm(Form):
    name = TextField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    time_estimate = TextField('time_estimate', validators=[DataRequired()])
    difficulty = TextField('difficulty', validators=[DataRequired()])
    submit = SubmitField()