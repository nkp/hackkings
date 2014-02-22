from hackkings.models.attachment import Attachment
from hackkings import db

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    completed = db.Column(db.Boolean, unique=False)
    #developers is back reffed
    state = db.Column(db.Integer, unique = False)
    proposer = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text, unique=False)
    #skills are back reffed
    #time in hours
    time_estimate = db.Column(db.Integer, unique=False)
    difficulty = db.Column(db.Integer, unique=False)
    attachments = db.relationship('Attachment', backref='project', lazy='dynamic')

    def __init__(self, name,completed,state,proposer,description,time_estimate,difficulty):
        self.name = name
        self.completed = completed
        self.state = state
        self.proposer = proposer
        self.description = description
        self.time_estimate = time_estimate
        self.difficulty = difficulty

    def __repr__(self):
        return '<Project %r>' % self.type

    def add_developer()