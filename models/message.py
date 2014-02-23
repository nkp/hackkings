from hackkings import db
from hackkings.models import MessageThread

class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('message_thread.id'))

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.DateTime)
    message = db.Column(db.Text)

    def __init__(self, thread, sender, message, time):
        self.thread = thread
        self.sender = sender
        self.message = message
        self.time = time

    def __repr__(self):
        return '<Message %r>' % self.message

    def validate__content(content):
        if len(content) > 5000:
            raise ValidationError('To be implemented')
