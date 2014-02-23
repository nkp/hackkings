from hackkings import db
from hackkings.models import MessageThread

from datetime import datetime

class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer, db.ForeignKey('message_thread.id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.DateTime, default=lambda ctx: datetime.utcnow())
    message = db.Column(db.Text)

    def __init__(self, thread, sender, message):
        self.thread = thread
        self.sender = sender
        self.message = message

    @classmethod
    def create(cls, thread, sender, message):
        new_message = Message(thread, sender, message)
        db.session.add(new_message)
        thread.messages.append(new_message)
        db.session.commit()

    def __repr__(self):
        return '<Message %r at %r>' % (self.message, str(self.time))

    def validate_content(content):
        if len(content) > 5000:
            raise ValidationError('To be implemented')
