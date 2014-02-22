from hackkings.models.attachment import Attachment
from hackkings import db

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    completed = db.Column(db.Boolean, unique=False)
    #developers is back reffed
    state = db.Column(db.Integer, db.ForeignKey('state.id'))
    proposer = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text, unique=False)
    #skills are back reffed
    #time in hours
    time_estimate = db.Column(db.Integer, unique=False)
    difficulty = db.Column(db.Integer, unique=False)
    attachments = db.relationship('Attachment', backref='project', lazy='dynamic')

    def __init__(self, name,developers,completed,state,proposer,description,skills_needed,time_estimate,difficulty,attachments):
        self.name = name
        self.developers = developers
        self.completed = completed
        self.state = state
        self.proposer = proposer
        self.description = description
        self.skills_needed = skills_needed
        self.time_estimate = time_estimate
        self.difficulty = difficulty
        self.attachments = attachments

    def __repr__(self):
        return '<Project %r>' % self.type