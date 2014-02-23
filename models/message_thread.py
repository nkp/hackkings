from hackkings.models import User
from hackkings import db
from hackkings.linkingtables import thread_link


class MessageThread(db.Model):
    __tablename__ = 'message_thread'
    id = db.Column(db.Integer, primary_key=True)
    messages = db.relationship('Message', backref='thread', lazy='dynamic')
    members = db.relationship('User', secondary=thread_link, 
                                        backref=db.backref('threads', lazy='dynamic')) 
    
    def __init__(self):
        pass

    def __repr__(self):
        return '<Thread %r>' % self.id 
   
    @classmethod
    def create(cls, new_members):
        new_thread = MessageThread()
        for member in new_members:
            new_thread.members.append(member)
        db.session.add(new_thread)
        db.session.commit()
        return new_thread
    
    @classmethod
    def find(cls, id):
        return MessageThread.query.filter_by(id = id).first()

    @classmethod
    def find_with_user(cls, user): 
        threads = []
        for thread in MessageThread.query.all():
            print thread.members
            if user in thread.members:
                threads.append(thread)
        return threads
        return MessageThread.query.filter(MessageThread.members.any(User.id == user.id))
