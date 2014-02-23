from flask_wtf import Form
from wtforms import TextField, RadioField, SubmitField, TextAreaField
from hackkings.models import Message, MessageThread
from wtforms.validators import DataRequired, ValidationError

class MessageReplyForm(Form):
    content = TextAreaField('Message content')
    submit  = SubmitField()


class MessageNewForm(Form):
    content    = TextAreaField('Message content')
    recipient  = TextField()
    submit     = SubmitField()



