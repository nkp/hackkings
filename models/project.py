from hackkings.models import Attachment
from hackkings.models import User
from hackkings import db
from sqlalchemy import or_
from hackkings.constants import STATES

class Project(db.Model):
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    completed = db.Column(db.Boolean, unique=False)
    #developers is back reffed
    state = db.Column(db.Integer, unique = False)
    proposer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
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

    def add_developer(self, id):
        dev = User.query.filter_by(id = id).first()
        if dev != None:
            self.developers.append(dev)
            self.state = STATES.ONGOING
            db.session.commit()

    def remove_developer(self, id):
        dev = self.developers.query.filter_by(id = id).first()
        if dev != None:
            self.developers.remove(dev)
            if !self.developers.query.all():
                self.state = STATES.PENDING
            db.session.commit()

    def find(self, id):
        return Project.filter_by(id = id).first()

    def get_skills(self):
        return self.skills.query.all()

    def get_current_developers(self):
        return self.developers.query.all()

    def get_all_current_projects(self):
        return Project.filter_by(or_(state = STATES.ONGOING, state = STATES.PENDING)).all() # Could be made more efficient by selecting only required columns
