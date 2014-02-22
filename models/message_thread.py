from hackkings.models import User
from hackkings import db
from hackkings.linkingtables import thread_link


class MessageThread(db.Model):
    __tablename__ = 'message_thread'
    id = db.Column(db.Integer, primary_key=True)
    members = db.relationship('Thread', secondary=thread_link, 
                                        backref=db.backref('users', lazy='dynamic')) 
    
    def __init__(self):
        pass

    def __repr__(self):
        return '<Thread %r>' % self.id 
    
