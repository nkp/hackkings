from hackkings.models.user import User
from hackkings import db

thread_link = db.Table('members', 
    db.Column('thread_id', db.Integer, db.ForeignKey('message_thread.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class MessageThread(db.Model):
    __tablename__ = 'message_thread'
    id = db.Column(db.Integer, primary_key=True)
    members = db.relationship('Thread', secondary=thread_link, 
                                        backref=db.backref('users', lazy='dynamic')) 
    
    def __init__(self):
        pass

    def __repr__(self):
        return '<Thread %r>' % self.id 
    
